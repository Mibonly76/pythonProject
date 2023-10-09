roll_of_paper = int(input())
roll_of_fabric = int(input())
amount_of_glue = float(input())
percent_discount = int(input()) / 100

price_of_paper = roll_of_paper * 5.80
price_of_fabric = roll_of_fabric * 7.20
price_of_glue = amount_of_glue * 1.20
total_sum = price_of_glue + price_of_fabric + price_of_paper
total_sum_with_discount = total_sum - total_sum * percent_discount

print(f"{total_sum_with_discount:.3f}")
