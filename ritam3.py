import json

# Read initial JSON data from environment_list.json
with open('environment_list.json', 'r') as file:
    data = json.load(file)

output = {}

for item in data:
    key = item['platform']
    value = f"{item['name']} -D browser={item['browser']} -D browser_version={item['version']}"
    if key in output:
        output[key].append(value)
    else:
        output[key] = [value]

# Save processed output to ritam2.json
with open('ritam2.json', 'w') as file:
    json.dump(output, file, indent=4)
