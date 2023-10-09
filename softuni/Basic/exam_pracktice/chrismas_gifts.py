# Инициализация на броячи и суми
total_adults = 0
total_kids = 0
total_toys_cost = 0
total_sweaters_cost = 0

# Четене на входни данни до команда "Christmas"
while True:
    input_data = input()
    if input_data == "Christmas":
        break

    age = int(input_data)

    # Определяне дали човекът е дете или възрастен и добавяне на разходи
    if age <= 16:
        total_kids += 1
        total_toys_cost += 5
    else:
        total_adults += 1
        total_sweaters_cost += 15

# Отпечатване на резултатите
print(f"Number of adults: {total_adults}")
print(f"Number of kids: {total_kids}")
print(f"Money for toys: {total_toys_cost}")
print(f"Money for sweaters: {total_sweaters_cost}")
