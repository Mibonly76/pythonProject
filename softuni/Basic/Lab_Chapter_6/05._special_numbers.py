divider = int(input())

for n in range(1111, 10000):
    for d in str(n):
        if int(d) == 0:
            break
        if divider % int(d) != 0:
            break
    else:
        print(n, end=" ")
