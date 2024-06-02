# name = input("Enter my name: ")
# print(name)

# this is a comment line


# Logic operators
# if not (5<4):
#     print(True)
# else:
#     print(False)

# Menbership Operators
colors = ["red", "green", "blue"]
x = "red"
# if x in colors:
#     print(True)
# else:
#     print(False)
#
# if x not in colors:
#     print(True)
# else:
#     print(False)


# age = 18
# if age  >18:
#     print("Watching sex")
# else:
#     print("Not watching sex")
# print("Next step")
#
# day = "Monday"
# if day == "Monday":
#     print("Today is Monday")
# elif day == "Tuesday":
#     print("Today is Tuesday")
# elif day == "Wednesday":
#     print("Today is Wednesday")
# else:
#     print("Unknown day!")
# print("Next step")
#
# a =4
# if a > 3:
#     pass
# print("Next step")
#
# match-case
# day = "Monday"
# match day:
#     case "Monday": print("Today is Monday")
#     case "Tuesday": print("Today is Tuesday")
#     case "Wednesday": print("Today is Wednesday")
#     case _: print("Invalid day")
# print("Next step")

"""
    Yêu cầu người dùng lần lượt nhập vào 2 số khác 0
    Tính và in ra màn hình tổng, hiệu, tích và thương
    của 2 số đó
"""
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# print("Sum: ", a +b)
# print("Subtractioin: ", a -b)
# print("Multiplication: ", a *b)
# print("Division: ", a /b)

"""
    Yêu cầu người dùng nhập vào 1 số nguyên tương ứng với số giờ
    In ra số giây tương ứng
"""
# hour = int(input("Enter the hour: "))
# second = hour *3600
# print("Number of seconds: ", second)

"""
    Yêu cầu người dùng nhập vào 1 số nguyên n
    Tính và in ra tổng số đo các góc của đa giác đều n cạnh
"""
# n = int(input("Enter a number: "))
# result = (n -2)*180
# print("Result:", result)

"""
    Yêu cầu người dùng nhập vào bán kính của hình tròn.
    Tính và hiển thị ra màn hình chu vi và diện tích của
    hình tròn tương ứng
"""
# from math import pi
#
# r = float(input("Enter the radius of the circle: "))
# # Circumference
# c = 2*r*pi
# # Area
# a = pi*(r**2)
# print("Circumference:", c)
# print("Area:", a)

"""
    lesson 3
    hàm thư viện và hàm tự định nghĩa
    định nghĩa hàm(functiion definition)
    def functiionName(param[optional])
        statements
        return value
    vi du:
    def sum(a, b):
        return a + b
    đối số vị trí(positional argument)
            từ khóa(keyword argument)
            mặc định(default argument)
        
"""


def sum(a, b):
    return a + b


# print(sum(3, 6))


def myF(a, b, c, d):
    """

    Parameters
    ----------
    a
    b
    c
    d

    Returns
    -------

    """


# print(sorted([3, 5, 6, 3]))

a = None
# print(a, type(a))

myList = ["red", "blue", "green", "yellow", "black"]
# print(myList[::-1])  # dung nhieu dao nguoc list
data1 = [1, 3, 5, 2, 9]
data1.append("kidbuu")
# print(data1)
data2 = [1, 3, 3, 5, 2, 9]
data2.sort()
print(data2)

# for index in (data):
#     print(index)
