digit = int(input())
digit_for_sum = int(input())

SUM_DIGITS = digit_for_sum

while SUM_DIGITS < digit:
    digit_for_sum = int(input())
    SUM_DIGITS += digit_for_sum
print(SUM_DIGITS)
