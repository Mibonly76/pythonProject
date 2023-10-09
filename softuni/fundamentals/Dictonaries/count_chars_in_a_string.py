input_list = [input_string for input_string in input() if input_string != " "]

output_dict = {}

for index in input_list:
    if index not in output_dict.keys():
        output_dict[index] = 0
    output_dict[index] += 1

for key, value in output_dict.items():
    print(f"{key} -> {value}")
