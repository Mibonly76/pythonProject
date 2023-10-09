from math import ceil

number_of_people = int(input())
ent_fee = float(input())
sun_bad = float(input())
sun_umbrella = float(input())

total_sum_ent = number_of_people * ent_fee
total_umbrellas = ceil(number_of_people / 2) * sun_umbrella
total_price_for_sunbeds = ceil(number_of_people * 0.75) * sun_bad

total_sum = total_sum_ent + total_umbrellas + total_price_for_sunbeds


print(f"{total_sum:.2f} lv.")
