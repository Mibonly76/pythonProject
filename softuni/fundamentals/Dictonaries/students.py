students = []
cource = " "

while True:

    input_string = input()

    if ":" not in input_string:
        cource = input_string
        break
    name, id, cource_name = input_string.split(":")
    students.append({"name": name, "id": id, "cource_name": cource_name})


for student in students:
    if cource.startswith(student["cource_name"][0:3]):
        print(f'{student["name"]} - {student["id"]}')
