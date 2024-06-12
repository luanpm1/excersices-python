data = {"name": "minh luan", "age": 9, "job": "AI engineer", "info": ["list", ("tuple")]}
print(data, type(data))
print(type(data))
print(data["name"])
print(data.get("name"))
data["gender"] = "male"
print(data)
data.pop("gender")
print(data)
del data["job"]
print(data)
print(data.keys())
print(data.values())
print(data.items())
