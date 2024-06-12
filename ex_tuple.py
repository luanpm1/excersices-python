data = ("minhluan", ["age", 9, True], {"gender": "male"}, {True:False})
print(data, ":", type(data))
data[-2]["gender"] = "female"
data[1][-1] = False
print(len(data))
print(data.count("minhluan"))




