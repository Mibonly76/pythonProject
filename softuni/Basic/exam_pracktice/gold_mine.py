num_locations = int(input())

total_actual_gold = 0
actual_average_gold_per_day = 0

for _ in range(num_locations):
    expected_gold_per_day = float(input())
    days = int(input())

    actual_gold_sum = 0

    for _ in range(days):
        actual_gold = float(input())
        actual_gold_sum += actual_gold

    actual_average_gold_per_day = actual_gold_sum / days

    if actual_average_gold_per_day >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {actual_average_gold_per_day:.2f}.")
    else:
        needed_gold = (expected_gold_per_day - actual_average_gold_per_day)
        print(f"You need {needed_gold:.2f} gold.")
