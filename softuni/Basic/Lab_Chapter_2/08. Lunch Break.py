from math import ceil

serial_name = input()
episode_time = int(input())
time_for_rest = int(input())

lunch_time = time_for_rest / 8
rest_time = time_for_rest / 4

total_time = lunch_time + rest_time + episode_time

if total_time < time_for_rest:
    print(f"You have enough time to watch {serial_name} and left with "
          f"{ceil(time_for_rest -total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, "
          f"you need {ceil(total_time - time_for_rest)} more minutes.")
