point = int(input())
BONUS = 0

if point <= 100:
    BONUS = 5
elif 100 < point <= 1000:
    BONUS = point * 0.2
else:
    BONUS = point * 0.1

if point % 2 == 0:
    BONUS += 1
elif point % 5 == 0:
    BONUS += 2

print(BONUS)
print(BONUS + point)
