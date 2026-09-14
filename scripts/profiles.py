#!/usr/bin/env python3
"""Validate source packs and compile self-contained native role bundles."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tomllib
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
LINK = re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)')


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def git(path, *args):
    return subprocess.check_output(['git', '-C', str(path), *args], text=True).strip()


def contained(root, path):
    path = path.resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes source: {path}')
    return path


def frontmatter(path):
    text = path.read_text()
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'{path}: missing YAML frontmatter')
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError(f'{path}: frontmatter must be a mapping')
    name, description = data.get('name'), data.get('description')
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64 or name != path.parent.name:
        raise ValueError(f'{path}: invalid or mismatched name')
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        raise ValueError(f'{path}: description must contain 1–1024 characters')
    return data, parts[2].lstrip('\n')


def link_target(file, target):
    target = target.strip().split(' "', 1)[0].strip('<>')
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
        return None
    target = unquote(target.split('#', 1)[0])
    return (file.parent / target).resolve() if target else None


def prose(text):
    return re.sub(r'^(`{3,}|~{3,}).*?^\1[^\n]*$', '', text, flags=re.M | re.S)


def check_links(file, root):
    for match in LINK.finditer(prose(file.read_text())):
        target = link_target(file, match[1])
        if target is not None:
            contained(root, target)
            if not target.exists():
                raise ValueError(f'{file}: missing reference {match[1]}')


def acyclic(graph):
    visited, active = set(), set()
    def visit(key):
        if key in active:
            raise ValueError(f'Dependency cycle at {key}')
        if key in visited:
            return
        if key not in graph:
            raise ValueError(f'Missing dependency: {key}')
        active.add(key)
        for dependency in graph[key]:
            visit(dependency)
        active.remove(key)
        visited.add(key)
    for key in graph:
        visit(key)


def load_packs(source_root, config, pinned=False):
    packs, skills, graph = {}, {}, {}
    for short, item in config['packs'].items():
        root = (source_root / item['repo']).resolve()
        catalog = read_json(root / 'directory.json')
        if catalog['name'] != item['id']:
            raise ValueError(f'{root}: pack identity mismatch')
        if pinned and git(root, 'rev-parse', 'HEAD') != item['sha']:
            raise ValueError(f'{root}: checkout does not match pinned commit')
        if pinned and git(root, 'status', '--porcelain', '--untracked-files=no', '--', 'skills', 'docs', 'agents', 'assets', 'scripts', 'directory.json', 'LICENSE', 'README.md'):
            raise ValueError(f'{root}: source content has uncommitted changes')
        packs[short] = {'root': root, 'catalog': catalog, **item}
        for name, entry in catalog['skills'].items():
            file = contained(root, root / entry['path'])
            data, body = frontmatter(file)
            if data['name'] != name:
                raise ValueError(f'{file}: catalog name differs')
            identifier = item['id'] + ':' + name
            if identifier in skills:
                raise ValueError(f'Duplicate identity: {identifier}')
            skills[identifier] = {'file': file, 'data': data, 'body': body, 'pack': short, 'name': name}
    pack_graph = {p['id']: p['catalog'].get('depends_on', []) for p in packs.values()}
    acyclic(pack_graph)
    ids = {p['repo']: p['id'] for p in packs.values()}
    ids.update({p['id']: p['id'] for p in packs.values()})
    for identifier, skill in skills.items():
        dependencies = skill['data'].get('metadata', {}).get('dependencies', [])
        if isinstance(dependencies, dict):
            dependencies = [dependencies]  # legacy source format; export one normalized form
        if not isinstance(dependencies, list):
            raise ValueError(f'{identifier}: dependencies must be a list')
        graph[identifier] = []
        for group in dependencies:
            if not isinstance(group, dict) or not isinstance(group.get('skills'), list):
                raise ValueError(f'{identifier}: invalid dependency group')
            source = group.get('source', 'self')
            pack_id = packs[skill['pack']]['id'] if source == 'self' else ids.get(source)
            if not pack_id:
                raise ValueError(f'{identifier}: unknown dependency source {source}')
            graph[identifier].extend(pack_id + ':' + name for name in group['skills'])
    acyclic(graph)
    for bundle, item in config['bundles'].items():
        available = {key for key, s in skills.items() if s['pack'] in item['packs']}
        for key in available:
            if set(graph[key]) - available:
                raise ValueError(f'{bundle}: incomplete dependency closure for {key}')
        for role in item['roles']:
            text = (ROOT / 'roles' / (role + '.md')).read_text()
            for ref in re.findall(r'igmarin/[a-z-]+:[a-z-]+', text):
                if ref not in available:
                    raise ValueError(f'{role}: unavailable skill {ref}')
    return packs, skills, graph


def source_files(pack):
    root = pack['root']
    files = {root / 'directory.json', root / 'LICENSE', root / 'README.md'}
    for folder in ('skills', 'docs', 'agents', 'assets', 'scripts'):
        if (root / folder).exists():
            files.update(p for p in (root / folder).rglob('*') if p.is_file() and '.DS_Store' not in p.parts and '__pycache__' not in p.parts and p.suffix != '.pyc')
    return sorted(p for p in files if p.is_file())


def validate_sources(packs, skills):
    for short, pack in packs.items():
        catalog_paths = {skill['file'].resolve() for skill in skills.values() if skill['pack'] == short}
        for file in source_files(pack):
            contained(pack['root'], file)
            if file.suffix == '.md' and file.is_relative_to(pack['root'] / 'skills'):
                check_links(file, pack['root'])
                if file.name == 'SKILL.md' and file.resolve() not in catalog_paths:
                    raise ValueError(f"{pack['id']}: unregistered skill {file}")
    return {'packs': len(packs), 'skills': len(skills), 'status': 'passed'}


def build(config, source_root, output, pinned=True):
    packs, skills, graph = load_packs(source_root, config, pinned)
    validate_sources(packs, skills)
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        staging = Path(temp)
        for bundle, specification in config['bundles'].items():
            dest = staging / bundle
            dest.mkdir()
            subset = {key: value for key, value in skills.items() if value['pack'] in specification['packs']}
            # Native names are stable across bundles; plugin namespaces isolate installations.
            names = {key: skill['pack'] + '-' + skill['name'] for key, skill in subset.items()}
            if len(set(names.values())) != len(names) or any(len(n) > 64 for n in names.values()):
                raise ValueError(f'{bundle}: emitted name collision or length violation')
            mapping, copies = {}, {}
            for short in specification['packs']:
                pack = packs[short]
                for file in source_files(pack):
                    target = dest / 'resources' / short / file.relative_to(pack['root'])
                    copies[file.resolve()] = target
            for key, skill in subset.items():
                mapping[skill['file'].resolve()] = dest / 'skills' / names[key] / 'SKILL.md'
            all_targets = {**copies, **mapping}
            def rewrite(text, original, target):
                def replace(match):
                    ref = link_target(original, match[1])
                    if ref is None:
                        return match[0]
                    translated = all_targets.get(ref)
                    if translated is None and ref.is_dir():
                        # Directory references retain their source-tree location.
                        for short in specification['packs']:
                            packroot = packs[short]['root']
                            if ref.is_relative_to(packroot):
                                translated = dest / 'resources' / short / ref.relative_to(packroot)
                                break
                    if translated is None:
                        return match[0]
                    fragment = '#' + match[1].split('#', 1)[1] if '#' in match[1] else ''
                    relative = os.path.relpath(translated, target.parent)
                    return match[0].replace(match[1], relative + fragment)
                return LINK.sub(replace, text)
            for original, target in copies.items():
                target.parent.mkdir(parents=True, exist_ok=True)
                if original.suffix == '.md':
                    target.write_text(rewrite(original.read_text(), original, target))
                else:
                    shutil.copy2(original, target)
            skill_map = {}
            for key, skill in subset.items():
                target = mapping[skill['file']]
                target.parent.mkdir(parents=True, exist_ok=True)
                data = skill['data']
                metadata = {'source-id': key, 'source-commit': packs[skill['pack']]['sha'],
                            'kind': classify(data.get('type', 'atomic'), skill['name']),
                            'dependencies': json.dumps(graph[key])}
                header = {'name': names[key], 'description': data['description'].strip(),
                          'license': data.get('license', 'MIT'), 'metadata': metadata}
                body = rewrite(skill['body'], skill['file'], target)
                notice = ('Resolve skill names through `../../skill-map.json`; use the source pack to disambiguate. '
                          'Load only the workflow and resources needed for the authorized task.\n\n')
                target.write_text('---\n' + yaml.safe_dump(header, sort_keys=False) + '---\n\n' + notice + body)
                skill_map[key] = {'name': names[key], 'path': str(target.relative_to(dest)), 'dependencies': graph[key]}
            common = (ROOT / 'roles' / 'common.md').read_text()
            for role in specification['roles']:
                text = (ROOT / 'roles' / (role + '.md')).read_text()
                title, body = text.split('\n', 1)
                description = title.lstrip('# ').strip()
                instructions = common + '\n' + body
                for key, name in names.items():
                    instructions = instructions.replace(key, f'{bundle}:{name} (skills/{name}/SKILL.md)')
                agent = dest / 'agents' / (role + '.md')
                agent.parent.mkdir(parents=True, exist_ok=True)
                agent.write_text('---\n' + yaml.safe_dump({'name': role, 'description': description}, sort_keys=False) + '---\n\n' + instructions)
                codex = dest / 'codex-agents' / (role + '.toml')
                codex.parent.mkdir(parents=True, exist_ok=True)
                codex.write_text('name = ' + json.dumps(role) + '\ndescription = ' + json.dumps(description) + '\ndeveloper_instructions = ' + json.dumps(instructions) + '\n')
                tomllib.loads(codex.read_text())
                entry = dest / 'skills' / role / 'SKILL.md'
                entry.parent.mkdir(parents=True, exist_ok=True)
                entry.write_text('---\n' + yaml.safe_dump({'name': role, 'description': description}, sort_keys=False) + '---\n\n' + instructions)
            manifest = {'name': bundle, 'version': config['version'], 'description': specification['description'], 'license': 'MIT', 'skills': './skills'}
            write_json(dest / '.devin-plugin' / 'plugin.json', manifest)
            write_json(dest / '.codex-plugin' / 'plugin.json', manifest)
            write_json(dest / 'skill-map.json', skill_map)
            aliases = {}
            for key, skill in subset.items():
                aliases.setdefault(skill['name'], []).append(key)
            write_json(dest / 'migration.json', {'remove_aliases_in': '2.0.0', 'aliases': {name: keys[0] for name, keys in aliases.items() if len(keys) == 1}, 'ambiguous': {name: keys for name, keys in aliases.items() if len(keys) > 1}})
            provenance = {short: {'id': packs[short]['id'], 'sha': packs[short]['sha'], 'sha256': {str(f.relative_to(packs[short]['root'])): hashlib.sha256(f.read_bytes()).hexdigest() for f in source_files(packs[short])}} for short in specification['packs']}
            write_json(dest / 'provenance.json', provenance)
        for bundle in config['bundles']:
            target = output / bundle
            if target.exists():
                shutil.rmtree(target)
            shutil.move(str(staging / bundle), target)
    return {'bundles': len(config['bundles']), 'skills': len(skills), 'pinned': pinned}


def classify(kind, name):
    if name in ('product-owner', 'project-manager', 'tech-lead', 'delivery-lead'):
        return 'role'
    return {'persona': 'workflow', 'playbook': 'workflow', 'orchestrator': 'router'}.get(kind, kind)


def validate_exports(output):
    count = 0
    for bundle in sorted(p for p in output.iterdir() if p.is_dir()):
        if (bundle / 'AGENTS.md').exists():
            raise ValueError(f'{bundle}: contributor instructions must not be always-on')
        for kind in ('.devin-plugin', '.codex-plugin'):
            manifest = read_json(bundle / kind / 'plugin.json')
            if manifest['name'] != bundle.name:
                raise ValueError(f'{bundle}: manifest name mismatch')
        skill_map = read_json(bundle / 'skill-map.json')
        for entry in skill_map.values():
            if not contained(bundle, bundle / entry['path']).is_file():
                raise ValueError(f'{bundle}: unavailable exported skill')
            if set(entry['dependencies']) - skill_map.keys():
                raise ValueError(f'{bundle}: incomplete exported dependency closure')
        for file in (bundle / 'skills').glob('*/SKILL.md'):
            frontmatter(file)
            check_links(file, bundle)
            count += 1
        for file in (bundle / 'codex-agents').glob('*.toml'):
            data = tomllib.loads(file.read_text())
            if set(data) != {'name', 'description', 'developer_instructions'}:
                raise ValueError(f'{file}: role changes host configuration')
    return {'entrypoints': count, 'status': 'passed'}


def validate_routing():
    checked = 0
    for fixture in sorted((ROOT / 'evals' / 'routing').glob('*.json')):
        data = read_json(fixture)
        role = ROOT / 'roles' / (data['role'] + '.md')
        text = (ROOT / 'roles' / 'common.md').read_text() + '\n' + role.read_text()
        for case in data['cases']:
            missing = set(case.get('requires', [])) - set(re.findall(r'igmarin/[a-z-]+:[a-z-]+', text))
            forbidden = set(case.get('forbids', [])) & set(re.findall(r'igmarin/[a-z-]+:[a-z-]+', text))
            if missing or forbidden or any(phrase not in text for phrase in case.get('requires_text', [])):
                raise ValueError(f"{fixture}:{case['id']}: routing contract mismatch")
            checked += 1
    return {'routing_cases': checked, 'status': 'passed'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['validate', 'build', 'check-exports', 'routing', 'pin', 'ledger'])
    parser.add_argument('--sources', type=Path, default=ROOT.parent)
    parser.add_argument('--output', type=Path, default=ROOT / 'plugins')
    parser.add_argument('--working-tree', action='store_true', help='Development build only; release builds require pinned clean source content')
    args = parser.parse_args()
    config = read_json(ROOT / 'profiles.json')
    try:
        if args.command == 'pin':
            for pack in config['packs'].values():
                pack['sha'] = git(args.sources / pack['repo'], 'rev-parse', 'HEAD')
            write_json(ROOT / 'profiles.json', config)
            result = {'status': 'pinned'}
        elif args.command == 'check-exports':
            result = validate_exports(args.output)
        elif args.command == 'routing':
            result = validate_routing()
        elif args.command == 'build':
            result = build(config, args.sources, args.output, not args.working_tree)
        else:
            packs, skills, graph = load_packs(args.sources, config)
            result = validate_sources(packs, skills)
            if args.command == 'ledger':
                ledger = read_json(ROOT / 'baseline' / 'capabilities.json')
                if {item['id'] for item in ledger} != set(skills):
                    raise ValueError('Capability inventory changed; supply explicit migration dispositions')
                for item in ledger:
                    skill = skills[item['id']]
                    item.update(kind=classify(skill['data'].get('type', 'atomic'), skill['name']), dependencies=graph[item['id']], current_commit=packs[skill['pack']]['sha'])
                    item['validation']['structural'] = 'passed'
                write_json(ROOT / 'reports' / 'capability-ledger.json', ledger)
        print(json.dumps(result))
    except (ValueError, KeyError, OSError, yaml.YAMLError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
