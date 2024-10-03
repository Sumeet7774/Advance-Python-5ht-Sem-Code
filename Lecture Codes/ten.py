#JSON (Javascript Object Notation) File Handling

import json

file_path = "data.json"

with open(file_path, "r") as json_file:
    data = json.load(json_file)
    
print(data)