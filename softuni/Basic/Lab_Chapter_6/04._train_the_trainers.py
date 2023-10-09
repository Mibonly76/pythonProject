n = int(input())

sum_of_grade = 0
total_grade_counter = 0
average_grade = 0
grade = 0

while True:
    presentation = input()
    if presentation == "Finish":
        print(f"Student's final assessment is {average_grade / total_grade_counter:.2f}.")
        break
    sum_of_grade = 0
    for _ in range(n):
        grade = float(input())
        sum_of_grade += grade
        total_grade_counter += 1

    average_grade += sum_of_grade

    print(f"{presentation} - {sum_of_grade / n:.2f}.")
