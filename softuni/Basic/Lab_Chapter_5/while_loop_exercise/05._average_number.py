n = int(input())
total_sum = 0

for _ in range(n):
    digit = int(input())
    total_sum += digit

print(f"{total_sum / n:.2f}")
