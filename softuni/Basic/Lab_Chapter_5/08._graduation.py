name = input()

year = 0
bad_counter = 0
total_sum_graduate = 0

while True:
    graduate = float(input())
    if graduate < 4.00:
        bad_counter += 1
        if bad_counter == 2:
            print(f"{name} has been excluded at {year + 1} grade")
            break
    else:
        year += 1
        total_sum_graduate += graduate

    if year == 12:
        print(f"{name} graduated. Average grade: {total_sum_graduate / 12:.2f}")
        break
