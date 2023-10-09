number = int(input())

star = "*"

for a in range(number):
    for b in range(number):
        print(star, end=" ") if b != (number - 1) else print(star)
