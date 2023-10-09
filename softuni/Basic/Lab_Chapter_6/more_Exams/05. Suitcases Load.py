capacity = float(input())
counter = 1
current_capacity = 0
number_of_suitcases = 0

while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    command = float(command)

    if counter == 3:
        counter = 1
        current_capacity += command * 1.1
    else:
        counter += 1
        current_capacity += command

    if current_capacity > capacity:
        print("No more space!")
        break
    number_of_suitcases += 1

print(f"Statistic: {number_of_suitcases} suitcases loaded.")
