food_list = input().split()

food_dict = {}

for i in range(0, len(food_list), 2):
    product = food_list[i]
    value = int(food_list[i + 1])
    food_dict[product] = value
print(food_dict)
