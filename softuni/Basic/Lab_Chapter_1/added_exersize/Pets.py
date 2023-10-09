from math import ceil, floor
days = int(input())
amount_of_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

dog_food *= days
cat_food *= days
turtle_food *= days
food_left = dog_food + cat_food + turtle_food

if food_left <= amount_of_food:
    print(f"{floor(amount_of_food - food_left)} kilos of food left.")
else:
    print(f"{ceil(food_left - amount_of_food)} more kilos of food are needed.")
