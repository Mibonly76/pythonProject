budget = float(input())
type_ticket = input()
number_people = int(input())

vip_tickets = number_people * 499.99
normal_tickets = number_people * 249.99

budget_for_transport = float()
result = float()

if 1 <= number_people <= 4:
    budget_for_transport = 0.75
elif 5 <= number_people <= 9:
    budget_for_transport = 0.6
elif 10 <= number_people <= 24:
    budget_for_transport = 0.5
elif 25 <= number_people <= 49:
    budget_for_transport = 0.4
elif number_people >= 50:
    budget_for_transport = 0.25

budget_for_tickets = budget - (budget * budget_for_transport)
budged_for_one = budget_for_tickets / number_people

if type_ticket == "VIP":
    if budget_for_tickets > vip_tickets:
        result = budget_for_tickets - vip_tickets
        print(f"Yes! You have {result:.2f} leva left.")
    else:
        result = vip_tickets - budget_for_tickets
        print(f"Not enough money! You need {result:.2f} leva.")

elif type_ticket == "Normal":
    if budget_for_tickets > normal_tickets:
        result = budget_for_tickets - normal_tickets
        print(f"Yes! You have {result:.2f} leva left.")
    else:
        result = normal_tickets - budget_for_tickets
        print(f"Not enough money! You need {result:.2f} leva.")
