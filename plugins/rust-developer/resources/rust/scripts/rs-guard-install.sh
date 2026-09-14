#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MANIFEST="$REPO_ROOT/bin/rs-guard.manifest"

if [[ ! -f "$MANIFEST" ]]; then
  echo "Missing rs-guard manifest: $MANIFEST" >&2
  exit 1
fi

read_manifest_value() {
  local key="$1"
  sed -n "s/^${key}=\"\(.*\)\"$/\1/p" "$MANIFEST" | head -n 1
}

RS_GUARD_VERSION="$(read_manifest_value RS_GUARD_VERSION)"
RS_GUARD_CRATE_VERSION="$(read_manifest_value RS_GUARD_CRATE_VERSION)"

: "${RS_GUARD_VERSION:?RS_GUARD_VERSION is required in bin/rs-guard.manifest}"
: "${RS_GUARD_CRATE_VERSION:?RS_GUARD_CRATE_VERSION is required in bin/rs-guard.manifest}"

if ! command -v cargo >/dev/null; then
  echo "cargo is required to install rs-guard ${RS_GUARD_CRATE_VERSION}." >&2
  exit 1
fi

INSTALL_DIR="${RS_GUARD_INSTALL_DIR:-$REPO_ROOT}"
OUTPUT_NAME="${RS_GUARD_OUTPUT_NAME:-rs-guard}"
OUTPUT_PATH="$INSTALL_DIR/$OUTPUT_NAME"
CARGO_ROOT="${RS_GUARD_CARGO_ROOT:-$INSTALL_DIR/.rs-guard-cargo-root}"

mkdir -p "$INSTALL_DIR" "$CARGO_ROOT"

echo "Installing rs-guard ${RS_GUARD_VERSION} from crates.io (${RS_GUARD_CRATE_VERSION})..."
cargo install rs-guard --locked --version "$RS_GUARD_CRATE_VERSION" --root "$CARGO_ROOT" --force

cp "$CARGO_ROOT/bin/rs-guard" "$OUTPUT_PATH"
chmod +x "$OUTPUT_PATH"

"$OUTPUT_PATH" --version

echo "rs-guard installed at $OUTPUT_PATH"
