
import json

# Read the raw lines from the file
with open("demo.json", "r") as file:
    lines = file.readlines()
formatted_json = json.dumps(data, indent=4)
with open("demo_fixed.json", "w") as outfile:
    outfile.write(formatted_json)

