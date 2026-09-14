import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('profiles', Path(__file__).resolve().parents[1] / 'scripts/profiles.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class ProfilesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.pack = self.root / 'example'
        self.skill = self.pack / 'skills' / 'sample'
        (self.skill / 'references').mkdir(parents=True)
        (self.skill / 'references' / 'details.md').write_text('Specific resource.\n')
        (self.skill / 'SKILL.md').write_text('---\nname: sample\ndescription: Handle a sample task.\n---\n\nRead [details](references/details.md).\n')
        p.write_json(self.pack / 'directory.json', {'name': 'igmarin/example', 'skills': {'sample': {'path': 'skills/sample/SKILL.md'}}})
        (self.pack / 'LICENSE').write_text('MIT\n')
        self.config = {'version': '0.1.0', 'packs': {'example': {'repo': 'example', 'id': 'igmarin/example', 'sha': 'a' * 40}}, 'bundles': {'sample-bundle': {'packs': ['example'], 'roles': [], 'description': 'Example bundle'}}}

    def test_build_preserves_references_and_is_reproducible(self):
        output = self.root / 'plugins'
        p.build(self.config, self.root, output, pinned=False)
        self.assertEqual(p.validate_exports(output)['status'], 'passed')
        skill = output / 'sample-bundle/skills/example-sample/SKILL.md'
        self.assertIn('../../resources/example/skills/sample/references/details.md', skill.read_text())
        self.assertEqual((output / 'sample-bundle/resources/example/skills/sample/references/details.md').read_text(), 'Specific resource.\n')
        before = {str(f.relative_to(output)): f.read_bytes() for f in output.rglob('*') if f.is_file()}
        p.build(self.config, self.root, output, pinned=False)
        self.assertEqual(before, {str(f.relative_to(output)): f.read_bytes() for f in output.rglob('*') if f.is_file()})

    def test_missing_and_cyclic_dependencies_fail(self):
        for graph in ({'a': ['b']}, {'a': ['b'], 'b': ['a']}):
            with self.assertRaises(ValueError):
                p.acyclic(graph)
        p.acyclic({'a': ['b'], 'b': []})

    def test_missing_reference_fails_without_replacing_existing_output(self):
        output = self.root / 'plugins'
        p.build(self.config, self.root, output, pinned=False)
        existing = (output / 'sample-bundle/skill-map.json').read_bytes()
        (self.skill / 'references/details.md').unlink()
        with self.assertRaisesRegex(ValueError, 'missing reference'):
            p.build(self.config, self.root, output, pinned=False)
        self.assertEqual(existing, (output / 'sample-bundle/skill-map.json').read_bytes())

    def test_symlink_cannot_import_outside_pack(self):
        outside = self.root / 'private.txt'
        outside.write_text('not part of the pack')
        (self.skill / 'leak.txt').symlink_to(outside)
        packs, skills, _ = p.load_packs(self.root, self.config)
        with self.assertRaisesRegex(ValueError, 'escapes source'):
            p.validate_sources(packs, skills)

    def test_real_yaml_types_and_name_are_checked(self):
        for header in ('name: sample\ndescription: [invalid]', 'name: different\ndescription: task'):
            (self.skill / 'SKILL.md').write_text('---\n' + header + '\n---\n')
            with self.assertRaises(ValueError):
                p.load_packs(self.root, self.config)

    def test_unavailable_dependency_is_not_replaced_with_general_skill(self):
        path = self.skill / 'SKILL.md'
        path.write_text(path.read_text().replace('description: Handle a sample task.', 'description: Handle a sample task.\nmetadata:\n  dependencies:\n    - source: self\n      skills: [absent]'))
        with self.assertRaisesRegex(ValueError, 'Missing dependency'):
            p.load_packs(self.root, self.config)

    def test_exported_dependency_closure_checked(self):
        output = self.root / 'plugins'
        p.build(self.config, self.root, output, pinned=False)
        path = output / 'sample-bundle/skill-map.json'
        data = p.read_json(path)
        data['igmarin/example:sample']['dependencies'] = ['igmarin/example:absent']
        p.write_json(path, data)
        with self.assertRaisesRegex(ValueError, 'incomplete exported dependency'):
            p.validate_exports(output)

    def test_code_examples_are_not_mistaken_for_required_links(self):
        path = self.skill / 'references/details.md'
        path.write_text('Example:\n```md\n[output](generated.md)\n```\n')
        p.check_links(path, self.pack)


if __name__ == '__main__':
    unittest.main()
