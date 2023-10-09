from math import ceil, floor

number_magnolii = int(input())
number_zumbuli = int(input())
number_roses = int(input())
number_cactus = int(input())
present_price = float(input())

MAGNOLIA = 3.25
ZUMBULI = 4
ROSES = 3.50
CACTUS = 8

total_price = \
    (number_magnolii * MAGNOLIA) \
    + (number_cactus * CACTUS) +\
    (number_zumbuli * ZUMBULI) + \
    (number_roses * ROSES)
total_price *= 0.95

if present_price <= total_price:
    print(f"She is left with {floor(total_price- present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - total_price)} leva.")
