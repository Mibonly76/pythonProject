number_of_students = int(input())

student_list = {}

for _ in range(number_of_students):
    name, graduate = input(), float(input())
    if name not in student_list.keys():
        student_list[name] = []
    student_list[name].append(graduate)

for key, value in student_list.items():
    averige_value = sum(value) / len(value)
    if averige_value >= 4.50:
        print(f"{key} -> {averige_value:.2f}")
