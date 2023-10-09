# Четене на броя на котките
num_cats = int(input())

# Инициализация на броячи за групите
group_1_count = 0
group_2_count = 0
group_3_count = 0

# Инициализация на общото количество храна
total_food = 0

# Четене на храната за всяка котка
for _ in range(num_cats):
    food = float(input())
    total_food += food

    if 100 <= food < 200:
        group_1_count += 1
    elif 200 <= food < 300:
        group_2_count += 1
    elif 300 <= food < 400:
        group_3_count += 1

# Изчисляване на цената за храната
price_per_kg = 12.45
total_price = (total_food / 1000) * price_per_kg

# Отпечатване на резултатите
print(f"Group 1: {group_1_count} cats.")
print(f"Group 2: {group_2_count} cats.")
print(f"Group 3: {group_3_count} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
