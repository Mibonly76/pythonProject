k = int(input())
s = int(input())
m = int(input())
n = int(input())

counter = 0
digit1 = 0
digit2 = 0


for num1 in range(k, 9):
    if num1 % 2 == 0:
        for num2 in range(s, 10):
            if num2 % 2 != 0:
                for num4 in range(m, 9):
                    if num4 % 2 == 0:
                        for num5 in range(n, 10):
                            if num5 % 2 != 0:
                                digit2 = f"{num4}{num5}"
                                digit2 = int(digit2)
                                igit1 = f"{num1}{num2}"
                                digit1 = int(digit1)
                                counter += 1
                                if digit1 == digit2:
                                    print("Cannot change the same player.")
                                else:
                                    print(f" {digit2} - {digit1}")
                                if counter == 6:
                                    exit()
