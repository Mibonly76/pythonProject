sice = int(input())

counter = 0

for row in range(0, sice + 1):
    for num in range(1, row + 1):
        counter += 1
        print(counter, end=" ") if row != num else print(counter)

        if counter == sice:
            exit()
