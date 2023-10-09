first_list = input().split(", ")
second_list = input().split(", ")

resul_list = []
for element_in_first_list in first_list:
    for element_in_second_list in second_list:
        if element_in_first_list in element_in_second_list:
            resul_list.append(element_in_first_list)
            break

print(resul_list)
