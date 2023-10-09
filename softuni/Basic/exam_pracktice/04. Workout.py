from math import ceil
amount_of_days = int(input())
km = float(input())

current_day_km = km
total_km = km


for day in range(amount_of_days):
    k = int(input()) / 100
    current_day_km += current_day_km * k
    total_km += current_day_km


if total_km < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_km)} more kilometers")
else:
    print(f"You've done a great job running {ceil(total_km - 1000)} more kilometers!")
