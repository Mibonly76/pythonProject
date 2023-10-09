number_of_students = int(input())
weak = 0
average = 0
good = 0
very_good = 0
average_grade = 0

for _ in range(number_of_students):
    grade_of_student = float(input())

    if 2.00 <= grade_of_student < 3:
        weak += 1
        average_grade += grade_of_student
    elif 3 <= grade_of_student < 4:
        average += 1
        average_grade += grade_of_student
    elif 4 <= grade_of_student < 5:
        good += 1
        average_grade += grade_of_student
    elif grade_of_student >= 5:
        very_good += 1
        average_grade += grade_of_student

print(f"Top students: {very_good / number_of_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good / number_of_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {average / number_of_students * 100:.2f}%")
print(f"Fail: {weak / number_of_students * 100:.2f}%")
print(f"Average: {average_grade / number_of_students:.2f}")
