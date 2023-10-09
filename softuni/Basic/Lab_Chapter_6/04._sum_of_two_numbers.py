low_interval_number = int(input())
hi_interval_number = int(input())
magic_number = int(input())

total_counter = 0
magic_number_found = False

for x1 in range(low_interval_number, hi_interval_number + 1):
    for x2 in range(low_interval_number, hi_interval_number + 1):
        total_counter += 1
        if (x1 + x2) == magic_number:
            magic_number_found = True
            break
    if magic_number_found:
        break
if not magic_number_found:
    print(f"{total_counter} combinations - neither equals {magic_number}")
else:
    print(f"Combination N:{total_counter} ({x1} + {x2} = {magic_number})")
