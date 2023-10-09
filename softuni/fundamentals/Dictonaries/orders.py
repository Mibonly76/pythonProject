product_dict = {}
value_1 = 0
value_2 = 0

while True:
    product = input()
    if product == "buy":
        break
    product = product.split()
    item, price, quantity = product
    if item not in product_dict.keys():
        product_dict[item] = [0.0 , 0.0]
    value_list = product_dict[item]
    value_1, value_2 = value_list
    value_1 = float(price)
    value_2 += float(quantity)
    product_dict[item] = [value_1, value_2]

for key, value in product_dict.items():
    price, quantity = value
    print(f"{key} -> {price * quantity:.2f}")
