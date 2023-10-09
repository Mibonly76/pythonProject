copmany_list = {}

while True:
    information_imput = input()
    if information_imput == "End":
        break
    company_name, employ_id = information_imput.split(" -> ")
    if company_name not in copmany_list.keys():
        copmany_list[company_name] = []
    if employ_id not in copmany_list[company_name]:
        copmany_list[company_name].append(employ_id)

for key, value in copmany_list.items():
    print(f"{key}")
    for element in value:
        print(f"-- {element}")
