# sample
data = ("minhluan", ["age", 9, True], {"gender": "male"}, {True: False})
print(data, ":", type(data))
data[-2]["gender"] = "female"
data[1][-1] = False
data_slice = data[1:3]
print(data_slice)
print(len(data))
print(data.count("minhluan"))
data1 = (1, 2, 3)  (3, 4, 5)
print(data1)
print(sorted(data1))
