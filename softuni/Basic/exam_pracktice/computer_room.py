# Четене на входните данни
month = input()
hours = int(input())
people = int(input())
time_of_day = input()

# Цени за час в зависимост от месеца и време на ден
if month in ["march", "april", "may"]:
    if time_of_day == "day":
        hourly_price = 10.50
    else:
        hourly_price = 8.40
elif month in ["june", "july", "august"]:
    if time_of_day == "day":
        hourly_price = 12.60
    else:
        hourly_price = 10.20

# Применяване на отстъпки
if people >= 4:
    hourly_price -= hourly_price * 0.10
if hours >= 5:
    hourly_price -= hourly_price * 0.50

# Изчисляване на общата цена
total_cost = (hourly_price * people) * hours

# Отпечатване на резултата
print(f"Price per person for one hour: {hourly_price:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
