# sample
data = {"name": "minh luan", "age": 9, "job": "AI engineer", "info": ["list", ("tuple")]}
print(data, type(data))
print(type(data))
print(data["name"])
print(data.get("name"))
data["gender"] = "male"
print(data)
# del
data.pop("gender")
print(data)
del data["job"]
print(data)
# get
print(data.keys())
print(data.values())
print(data.items())
dict1 = {"name": "minhluan"}
dict2 = {"age": "9"}
tong = dict1["name"] + dict2["age"]
print(tong)
