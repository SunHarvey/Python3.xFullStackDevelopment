import json

data = {"name": "wangwu", "age": 23, "language": ("python", "java")}
data_json = json.dumps(data, indent=2)
print(data_json, type(data_json))
