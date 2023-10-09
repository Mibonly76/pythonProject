number = int(input())

max_number = float('-inf')
max_sum = 0

for _ in range(number):
    dig = int(input())

    if dig > max_number:
        max_number = dig
    max_sum += dig

if (max_sum - max_number) == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_sum - max_number - max_number)}")
