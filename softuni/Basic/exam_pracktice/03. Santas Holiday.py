amount_of_days = int(input()) - 1
type_of_room = input()
gaduate = input()

price = 0

if amount_of_days < 10:
    if type_of_room == "room for one person":
        price = amount_of_days * 18
    elif type_of_room == "apartment":
        price = amount_of_days * 25
        price = price - price * 0.30
    else:
        price = amount_of_days * 35
        price = price - price * 0.10


elif 10 <= amount_of_days <= 15:
    if type_of_room == "room for one person":
        price = amount_of_days * 18
    elif type_of_room == "apartment":
        price = amount_of_days * 25
        price = price - price * 0.35
    else:
        price = amount_of_days * 35
        price = price - price * 0.15
else:
    if type_of_room == "room for one person":
        price = amount_of_days * 18
    elif type_of_room == "apartment":
        price = amount_of_days * 25
        price = price - price * 0.50
    else:
        price = amount_of_days * 35
        price = price - price * 0.20

if gaduate == "positive":
    print(f"{price + price * 0.25:.2f}")
else:
    print(f"{price - price * 0.10:.2f}")
