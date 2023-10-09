number = int(input())

ko = number * 2 - 2
spaces = " " * number
stars = "*" * number * 2
semi_column = '/' * ko
column = "|" * number
index = abs((number + 1) // 2 - 1)

for row in range(number):
    if row == 0 or row == number - 1:
        print(stars, end="")
        print(spaces, end="")
        print(stars)
    elif row == index:
        print("*" + semi_column + "*", end="")
        print(column, end="")
        print("*" + semi_column + "*")
    else:
        print("*" + semi_column + "*", end="")
        print(spaces, end="")
        print("*" + semi_column + "*")
