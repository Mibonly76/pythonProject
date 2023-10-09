number = int(input())

for row in range(number + 1):
    stars = "*" * row
    space = " " * (number - row)
    print(space, end="")
    print(stars, end="")
    print(" | ", end="")
    print(stars, end="")
    print()
