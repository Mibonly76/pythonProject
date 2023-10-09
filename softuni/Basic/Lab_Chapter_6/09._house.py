from math import ceil
number = int(input())

roof_length = ceil(number / 2)

star = 1
dashes = 1

# top of the roof
for row in range(roof_length):
    if number % 2 == 0:
        star += 1
        dashes = (number - star) // 2
        print("-" * dashes, end="")
        print("*" * star, end="")
        print("-" * dashes)
    else:
        dashes = (number - star) // 2
        print("-" * dashes, end="")
        print("*" * star, end="")
        print("-" * dashes)
        star += 1
    star += 1

# Body
for row in range(number // 2):
    print("|" + ("*" * (number - 2)) + "|")
