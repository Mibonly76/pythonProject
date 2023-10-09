first_employ = int(input())
second_employ = int(input())
third_employ = int(input())
number_of_students = int(input())
total_time_per_per = first_employ + second_employ + third_employ
total_time = 0
while number_of_students > 0:
    if not number_of_students <= 0:
        number_of_students -= total_time_per_per
        total_time += 1
        if total_time % 4 == 0:
            total_time += 1

else:
    print(f"Time needed: {total_time}h.")
