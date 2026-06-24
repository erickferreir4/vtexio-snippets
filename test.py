import json, glob, os
errors = []
for fp in ['snippets.json'] + sorted(glob.glob('snippets/**/*.json', recursive=True)):
    try:
        with open(fp) as f:
            json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f'{fp}: {e}')
if errors:
    for e in errors:
        print('ERROR:', e)
else:
    print('All JSON files are valid')
