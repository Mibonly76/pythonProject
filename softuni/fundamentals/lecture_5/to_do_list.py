
to_do_list = ["None"] * 10
index = 0
while True:
    to_do_list_element = input()

    if to_do_list_element == "End":
        for element in range(0, 9):
            if to_do_list[element] == "None":
                to_do_list.remove("None")
        print(to_do_list)
        break
    to_do_list_element = to_do_list_element.split("-")

    index = int(to_do_list_element[0])
    to_do_list.pop(index)
    to_do_list.insert(index, to_do_list_element[1])
