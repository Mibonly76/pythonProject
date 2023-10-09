number = int(input())

star = "*"
space = " "

for row in range(1, number + 1):
    for poz in range(1, number - row + 1):
        print(space, end="")
    print(star, end="")

    for poz in range(1, row):
        print(f" {star}", end="")
    print()


for row in range(number, 0, -1):
    for poz in range(1, number - row + 1):
        print(space, end="")

    for poz in range(1, row):
        print(f" {star}", end="")
    print()
