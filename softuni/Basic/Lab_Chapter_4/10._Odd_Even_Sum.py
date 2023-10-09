number = int(input())

even_sum = 0
odd_sum = 0

for num in range(number):
    if (num % 2) == 0:
        odd_sum += int(input())
    else:
        even_sum += int(input())

if even_sum == odd_sum:
    print(f"Yes\nSum = {odd_sum}")
else:
    print(f"No\nDiff = {abs(even_sum - odd_sum)}")
