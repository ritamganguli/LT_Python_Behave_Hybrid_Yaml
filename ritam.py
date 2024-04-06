import json

# Read data from the JSON file
with open('environment_list.json', 'r') as file:
    data = json.load(file)

platforms = {}

# Organize data by platform
for item in data:
    platform = item['platform']
    feature = item['name']
    if platform in platforms:
        platforms[platform].append(feature)
    else:
        platforms[platform] = [feature]

# Convert to the desired format
result = {}
for platform, features in platforms.items():
    result[platform] = features

# Write the result to a file
with open('ritam2.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)

print("Data saved to data.json.")
