nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

BAGS = 0.40
NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00


nylon += 2
nylon *= NYLON_PRICE

paint += paint * 0.1

paint *= PAINT_PRICE
thinner *= THINNER_PRICE

amount_goods = nylon + paint + thinner + BAGS

work_for_one_hour = amount_goods * 0.3

total_price = amount_goods + (work_for_one_hour * work_hours)

print(total_price)
