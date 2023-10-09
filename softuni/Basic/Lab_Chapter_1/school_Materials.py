amount_pencils = int(input())
amount_markers = int(input())
detergent_litres = int(input())
discount = int(input())/100

PENCILS_PRICE = 5.80
MARKERS_PRICE = 7.20
DETERGENT_PRICE = 1.2

amount_pencils *= PENCILS_PRICE
amount_markers *= MARKERS_PRICE
detergent_litres *= DETERGENT_PRICE

amount_no_discount = amount_pencils + amount_markers + detergent_litres
total_discount = amount_no_discount - (amount_no_discount * discount)


print(total_discount)
