price_holiday = float(input())

amount_puzzles = int(input())
amount_doles = int(input())
amount_teddies = int(input())
amount_minions = int(input())
amount_trucks = int(input())

PRICE_PUZZLES = 2.6
PRICE_DOLES = 3
PRICE_TEDDIES = 4.10
PRICE_MINIONS = 8.20
PRICE_TRUCKS = 2

total_amount = \
    amount_puzzles + \
    amount_doles + \
    amount_teddies + \
    amount_minions + \
    amount_trucks

total_price = \
    (amount_puzzles * PRICE_PUZZLES) + \
    (amount_doles * PRICE_DOLES) + \
    (amount_teddies * PRICE_TEDDIES) + \
    (amount_minions * PRICE_MINIONS) + \
    (amount_trucks * PRICE_TRUCKS)

if total_amount >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price < price_holiday:
    print(f"Not enough money! {price_holiday - total_price:.2f} lv needed.")
else:
    print(f"Yes! {total_price - price_holiday:.2f} lv left.")
