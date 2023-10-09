budget = float(input())
season = input()

expense = 0
facility = None
location = None

if budget > 1000:
    expense = budget * 0.90
    facility = "Hotel"
    location = "Europe"
elif 101 <= budget <= 1000:
    if season == "summer":
        expense = budget * 0.40
        facility = "Camp"
    elif season == "winter":
        expense = budget * 0.80
        facility = "Hotel"
    location = "Balkans"
elif budget <= 100:
    if season == "summer":
        expense = budget * 0.30
        facility = "Camp"
    elif season == "winter":
        expense = budget * 0.70
        facility = "Hotel"
    location = "Bulgaria"

print(f"Somewhere in {location}")
print(f"{facility} - {expense:.2f}")
