number = int(input())

star = "$"

for row in range(1, number + 1):
    for b in range(1, row + 1):
        print(star, end=" ") if b != row else print(star)
