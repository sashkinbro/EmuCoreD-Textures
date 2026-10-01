"""Validate textures.json against schemas/texture-catalog.schema.json."""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
catalog = json.loads((root / 'textures.json').read_text(encoding='utf-8'))
assert catalog['schemaVersion'] == 1, 'unexpected schema version'
assert catalog['platform'] == 'azahar', 'unexpected platform'
for entry in catalog['entries']:
    assert entry['titleIds'], f"{entry['id']}: no title ids"
    assert entry['distribution'] in ('link-only', 'mirrored')
print(f"ok: {len(catalog['entries'])} entries")
