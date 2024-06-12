# List
data = ["minh luan", 9, True, ("male"), {"job": "AI engineer"}]
print(data, type(data))
print(data[1])
print(data[0:2])
# add
data.insert(data[1], ["AI engineer"])
print(data)
data.append(["hello world"])
print(data)
data.extend(["wellcome to python"])
print(data)
data += ("computer")
print(data)
# delete
data.pop(6)
print(data)
del data[5]
print(data)
del data[4:6]
print(data)
data.remove("m")
print(data)
# data.clear()
# print(data)
data.reverse()
print(data)
print(data.count("minh luan"))
print(data[::-1])
