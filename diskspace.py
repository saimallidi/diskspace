import os
import sys
import json

files = os.listdir(sys.argv[1])
resp_files = []

for file in files:
  path = sys.argv[1] + "/" + file
  size = os.path.getsize(path)
  resp_files.append({path:size})

response = {
  "files": resp_files
}

print(json.dumps(response,indent=0))
