from math import floor
from math import ceil

wine_area = int(input())
amount_of_grapes = float(input())
amount_of_wine = int(input())
workers = int(input())

grapes_for_wine = wine_area * amount_of_grapes * 0.4 / 2.5

if grapes_for_wine < amount_of_wine:
    print(f"It will be a tough winter! More {floor(amount_of_wine - grapes_for_wine)} liters wine needed.")
else:
    wine_left = grapes_for_wine - amount_of_wine
    print(f"Good harvest this year! Total wine: {floor(grapes_for_wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_left / workers)} liters per person.")
