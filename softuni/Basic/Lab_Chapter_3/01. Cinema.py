PROJECTION = input()
rows = int(input())
columns = int(input())

PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

price = 0.0

cinema_capacity = rows * columns

if PROJECTION == "Premiere":
    price = cinema_capacity * PREMIERE
elif PROJECTION == "Normal":
    price = cinema_capacity * NORMAL
elif PROJECTION == "Discount":
    price = cinema_capacity * DISCOUNT

print(f"{price:.2f} leva")
