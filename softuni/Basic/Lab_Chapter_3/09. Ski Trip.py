days = int(input()) - 1
room = input()
rating = input()

price = 0
ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

if days < 10:
    if room == "room for one person":
        price = ROOM_FOR_ONE_PERSON * days
    elif room == "apartment":
        price = APARTMENT * days * 0.70
    elif room == "president apartment":
        price = PRESIDENT_APARTMENT * days * 0.90
elif 10 <= days <= 15:
    if room == "room for one person":
        price = ROOM_FOR_ONE_PERSON * days
    elif room == "apartment":
        price = APARTMENT * days * 0.65
    elif room == "president apartment":
        price = PRESIDENT_APARTMENT * days * 0.85
else:
    if room == "room for one person":
        price = ROOM_FOR_ONE_PERSON * days
    elif room == "apartment":
        price = APARTMENT * days * 0.50
    elif room == "president apartment":
        price = PRESIDENT_APARTMENT * days * 0.80

if rating == "positive":
    price = price + price * 0.25
elif rating == "negative":
    price *= 0.90
print(f"{price:.2f}")
