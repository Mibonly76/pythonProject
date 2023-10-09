month = input()
numbers_of_nights = int(input())

apartment = None
studio = None

if month == "May" or month == "October":
    apartment = f"Apartment: {numbers_of_nights * 65:.2f} lv."
    studio = f"Studio: {numbers_of_nights * 50:.2f} lv."
    if 7 < numbers_of_nights <= 14:
        studio = f"Studio: {numbers_of_nights * 50 * 0.95:.2f} lv."
    elif numbers_of_nights > 14:
        studio = f"Studio: {numbers_of_nights * 50 * 0.70:.2f} lv."
        apartment = f"Apartment: {65 * numbers_of_nights * 0.90:.2f} lv."
elif month == "June" or month == "September":
    apartment = f"Apartment: {numbers_of_nights * 68.70:.2f} lv."
    studio = f"Studio: {numbers_of_nights * 75.20:.2f} lv."
    if numbers_of_nights > 14:
        studio = f"Studio: {numbers_of_nights * 75.20 * 0.80:.2f} lv."
        apartment = f"Apartment: {68.70 * numbers_of_nights * 0.90:.2f} lv."
elif month == "July" or month == "August":
    apartment = f"Apartment: {numbers_of_nights * 77:.2f} lv."
    studio = f"Studio: {numbers_of_nights * 76:.2f} lv."
    if numbers_of_nights > 14:
        apartment = f"Apartment: {numbers_of_nights * 77 * 0.90:.2f} lv."


print(apartment)
print(studio)

