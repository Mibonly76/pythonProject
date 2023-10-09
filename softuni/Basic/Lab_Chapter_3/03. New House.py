plant = input()
amount_of_plant = int(input())
budged = int(input())

plant_price = 0

if plant == "Roses":
    plant_price = amount_of_plant * 5
    if amount_of_plant > 80:
        plant_price *= 0.90
elif plant == "Dahlias":
    plant_price = amount_of_plant * 3.80
    if amount_of_plant > 90:
        plant_price *= 0.85
elif plant == "Tulips":
    plant_price = amount_of_plant * 2.80
    if amount_of_plant > 80:
        plant_price *= 0.85
elif plant == "Narcissus":
    plant_price = amount_of_plant * 3
    if amount_of_plant < 120:
        plant_price += plant_price * 0.15
elif plant == "Gladiolus":
    plant_price = amount_of_plant * 2.50
    if amount_of_plant < 80:
        plant_price += plant_price * 0.20

if budged >= plant_price:
    print(f"Hey, you have a great garden with {amount_of_plant} {plant} and {budged - plant_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {plant_price - budged:.2f} leva more.")
