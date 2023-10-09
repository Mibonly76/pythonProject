number = int(input())

plus = "+"
minus = "-"
colum = "|"

for row in range(number, 0, -1):
    if row == number or row == 1:
        for poz in range(1, number + 1):
            if poz == 1:
                print(plus, end=" ")
            elif poz == number:
                print(plus)
            else:
                print(minus, end=" ")
    else:
        for poz in range(1, number + 1):
            if poz == 1:
                print(colum, end=" ")
            elif poz == number:
                print(colum)
            else:
                print(minus, end=" ")
