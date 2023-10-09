EXPECTED_SUM = int(input())

counter = 1
cs_counter = 0
cs_amount = 0
cc_counter = 0
cc_amount = 0

while True:

    if (cs_amount + cc_amount) >= EXPECTED_SUM:
        print(f"Average CS: {cs_amount / cs_counter:.2f}\nAverage CC: {cc_amount / cc_counter:.2f}")
        break

    sum_to_pay = input()

    if sum_to_pay == "End":
        print("Failed to collect required money for charity.")
        break

    price = int(sum_to_pay)
    counter += 1

    if (counter % 2) != 0 and price <= 100:  # pay in cache
        print("Product sold!")
        cs_amount += price
        cs_counter += 1

    elif (counter % 2) == 0 and price >= 10:  # pay with card

        cc_counter += 1
        cc_amount += price

    else:
        print("Error in transaction!")
        continue

    print("Product sold!")
