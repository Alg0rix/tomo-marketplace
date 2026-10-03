"""Build the community catalog from reviewed submission metadata."""
import json
from pathlib import Path
import jsonschema

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / "schema/plugin-entry.schema.json").read_text())
plugins = []
for path in sorted((root / "plugins").glob("*.json")):
    entry = json.loads(path.read_text())
    jsonschema.validate(entry, schema)
    assert path.stem == entry["id"], "Submission filename must match plugin id"
    plugins.append(entry)
ids = [entry["id"] for entry in plugins]
assert len(ids) == len(set(ids)), "Duplicate plugin identities"
manifest = {"schema_version": 1, "id": "tomo-community", "name": "Tomo Community", "plugins": plugins}
(root / "marketplace.json").write_text(json.dumps(manifest, indent=2) + "\n")
