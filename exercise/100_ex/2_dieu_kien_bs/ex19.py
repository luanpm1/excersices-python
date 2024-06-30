"""
    Giải và biện luận phương trình ax^2 + bx + c = 0
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))

if a != 0:
    delta = b * b - 4 * (a * c)
    print(delta)
    if delta > 0:
        print("x1:", (-b + delta * 0.5) / 2 * a)
        print("x2:", ((-b - delta * 0.5) / 2 * a))
    elif: