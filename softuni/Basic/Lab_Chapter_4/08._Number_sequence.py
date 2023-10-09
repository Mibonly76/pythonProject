from sys import maxsize
number = int(input())

max_number = -maxsize
min_number = maxsize

for num in range(number):
    digit = int(input())

    if digit > max_number:
        max_number = digit

    if digit < min_number:
        min_number = digit

print(f"Max number: {max_number} \nMin number: {min_number}")
