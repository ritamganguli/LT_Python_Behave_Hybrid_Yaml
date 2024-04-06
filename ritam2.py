import os
import json
import sys

# Read platform from environment variable
platform = os.environ.get("HYPEREXECUTE_PLATFORM")
os_env= platform

# Read JSON data from file
with open("ritam2.json", "r") as file:
    json_data = file.read()

# Load JSON data
data = json.loads(json_data)

# Print elements according to the platform
if platform in data and platform!="macos Ventura" and platform!="macos Monterey":
    for item in data[platform]:
        print("features/"+item)
elif platform=="macos Ventura":
    for item in data["macos Ventura"]:
        # print("macos Ventura")
        print("features/"+item)
elif platform=="macos Monterey":
    for item in data["macos Monterey"]:
        # print("macos Ventura")
        print("features/"+item)
else:
    print("Platform not found in JSON data. ")
    print(os.environ.get("os"))
    print(os.environ.get("HYPEREXECUTE_PLATFORM"))
    sys.exit(1)  # Exit with non-zero exit code