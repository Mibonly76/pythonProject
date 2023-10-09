cource_list = {}

while True:
    cource_information = input()
    if cource_information == "end":
        break
    course_name, student_name = cource_information.split(" : ")
    if course_name not in cource_list.keys():
        cource_list[course_name] = []
    cource_list[course_name].append(student_name)

for key, value in cource_list.items():
    print(f"{key}: {len(value)}")
    for element in value:
        print(f"-- {element}")
