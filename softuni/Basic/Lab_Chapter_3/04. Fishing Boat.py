budged = int(input())
season = input()
amount_of_fishers = int(input())

total_price = 0

if season == "Spring":
    ship_rend = 3000
    if amount_of_fishers <= 6:
        total_price = ship_rend * 0.9
    elif 7 <= amount_of_fishers <= 11:
        total_price = ship_rend * 0.85
    elif amount_of_fishers >= 12:
        total_price = ship_rend * 0.75
elif season == "Summer" or season == "Autumn":
    ship_rend = 4200
    if amount_of_fishers <= 6:
        total_price = ship_rend * 0.9
    elif 7 <= amount_of_fishers <= 11:
        total_price = ship_rend * 0.85
    elif amount_of_fishers >= 12:
        total_price = ship_rend * 0.75
elif season == "Winter":
    ship_rend = 2600
    if amount_of_fishers <= 6:
        total_price = ship_rend * 0.9
    elif 7 <= amount_of_fishers <= 11:
        total_price = ship_rend * 0.85
    elif amount_of_fishers >= 12:
        total_price = ship_rend * 0.75

if season != "Autumn" and amount_of_fishers % 2 == 0:
    total_price *= 0.95

if budged >= total_price:
    print(f"Yes! You have {budged - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budged:.2f} leva.")
