money = float(input())
end_year = int(input()) + 1

money_left = money
age = 17
set_fee = 0

for cur_year in range(1800, end_year):
    age += 1
    if cur_year % 2 == 0:
        money_left -= 12000
        if cur_year == end_year:
            set_fee = 12000
            break
    else:
        current_fee = 12000 + 50 * age
        money_left -= current_fee
        if cur_year == end_year:
            set_fee = current_fee
            break

if money_left >= set_fee:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")

else:
    print(f"He will need {set_fee - money_left:.2f} dollars to survive.")
