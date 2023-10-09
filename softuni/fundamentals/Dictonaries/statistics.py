product_in_stock = {}
temp_product_list = []
sum_value_of_elemetnt = 0
while True:
    input_value = input()
    if input_value == "statistics":
        break

    temp_product_list = input_value.split(": ")
    if temp_product_list[0] not in product_in_stock:
        product_in_stock[temp_product_list[0]] = int(temp_product_list[1])
    else:
        product_in_stock[temp_product_list[0]] += int(temp_product_list[1])

    temp_product_list = []
amount_of_products = len(product_in_stock)

for elemen in product_in_stock.keys():
    sum_value_of_elemetnt += product_in_stock[elemen]

print("Products in stock:")
for elemens in product_in_stock:
    print(f"- {elemens}: {product_in_stock[elemens]}")

print(f"Total Products: {amount_of_products}")
print(f"Total Quantity: {sum_value_of_elemetnt}")
