from math import pi
figure = input()
the_area = 0

if figure == "square":
    a = float(input())
    the_area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    the_area = a * b
elif figure == "circle":
    r = float(input())
    the_area = pi * r * r
elif figure == "triangle":
    a = float(input())
    h = float(input())
    the_area = a * h / 2

print(f"{the_area:.3F}")
