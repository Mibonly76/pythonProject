stok_list = input().split()

stok_dict = {}

for i in range(0, len(stok_list), 2):
    product = stok_list[i]
    value = stok_list[i + 1]
    stok_dict[product] = value

search_list = input().split()

for item in search_list:
    if item in stok_dict.keys():
        print(f"We have {stok_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
