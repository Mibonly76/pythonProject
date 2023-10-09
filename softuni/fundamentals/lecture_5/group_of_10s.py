from math import ceil

list_of_numbers = [int(digit) for digit in (input().split(", "))]

max_number = ceil(max(list_of_numbers) / 10)
temp_list = []
row_indicator = 0

for row_index in range(1, max_number + 1):
    row_indicator = row_index * 10
    for element_from_list in list_of_numbers:
        if element_from_list <= row_indicator:
            temp_list.append(element_from_list)

    print(f"Group of {row_indicator}\'s: {temp_list}")

    for element in list_of_numbers[::-1]:
        if element <= row_indicator:
            list_of_numbers.remove(element)
    temp_list = []
