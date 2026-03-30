# Schemas

This directory contains JSON schemas for the hackathon toolkit's data formats.

## score-input.json

Defines the expected format for the CSV input to `scripts/score_calc.py`.

This schema documents the contract — it doesn't enforce it at runtime (the script validates input directly). It's here for documentation and for anyone building tooling on top of the score calculator.

Validate an example file against the schema:
```bash
pip install jsonschema
python3 -c "
import json, jsonschema
schema = json.load(open('schemas/score-input.json'))
data = json.load(open('schemas/example-scores.json'))
jsonschema.validate(data, schema)
print('Valid.')
"
```
