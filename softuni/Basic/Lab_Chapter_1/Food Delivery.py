chicken = int(input())
fish = int(input())
vegan = int(input())

CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEGAN_PRICE = 8.15
DELIVERY = 2.50

food_price = (chicken * CHICKEN_PRICE) + (fish * FISH_PRICE) + (vegan * VEGAN_PRICE)
desert_price = food_price * 0.2
total_price = food_price + desert_price + DELIVERY

print(total_price)
