import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

total_aprons = math.ceil(students * 1.2)
total_flour = students - (students // 5)

total_cost = (total_aprons * price_apron) + (total_flour * price_flour) + (students * 10 * price_egg)

if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")
