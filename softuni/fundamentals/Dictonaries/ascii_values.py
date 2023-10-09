input_list = input().split(", ")

# ascii_dict = {}
#
# for item in input_list:
#     ascii_dict[item] = ord(item)

ascii_dict = {key: ord(key) for key in input_list}

print(ascii_dict)
