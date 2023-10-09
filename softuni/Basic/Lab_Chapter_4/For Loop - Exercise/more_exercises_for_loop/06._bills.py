months = int(input())

WATER = 0
INTERNET = 0
other = 0
fee = 0
electricity = 0

for _ in range(months):
    electricity += float(input())
    WATER += 20
    INTERNET += 15

other = (1.2 * WATER) + (1.2 * electricity) + (1.2 * INTERNET)
fee = electricity + INTERNET + WATER + other

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {WATER:.2f} lv")
print(f"Internet: {INTERNET:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {fee / months:.2f} lv")
