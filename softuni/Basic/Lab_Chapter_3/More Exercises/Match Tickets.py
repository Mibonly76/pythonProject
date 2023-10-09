budged = float(input())
type_ticket = input()
number_people = int(input())

IP = 499.99
NORMAL = 249.99
real_budged = 0.00
budged_for_one = 0.00
result = None
ip_people = number_people * IP
normal_people = number_people * NORMAL

if 1 <= number_people <= 4 and type_ticket == "VIP":
    transport = budged * 0.75
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= IP:
        result = f"Yes! You have {real_budged - ip_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {ip_people - real_budged:.2f} leva."
elif 1 <= number_people <= 4 and type_ticket == "Normal":
    transport = budged * 0.75
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= NORMAL:
        result = f"Yes! You have {real_budged - normal_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {normal_people - real_budged:.2f} leva."

elif 5 <= number_people <= 9 and type_ticket == "VIP":
    transport = budged * 0.60
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= IP:
        result = f"Yes! You have {real_budged - ip_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {ip_people - real_budged:.2f} leva."
elif 5 <= number_people <= 9 and type_ticket == "Normal":
    transport = budged * 0.60
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= NORMAL:
        result = f"Yes! You have {real_budged - normal_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {normal_people - real_budged:.2f} leva."

elif 10 <= number_people <= 24 and type_ticket == "VIP":
    transport = budged * 0.50
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= IP:
        result = f"Yes! You have {real_budged - ip_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {ip_people - real_budged:.2f} leva."
elif 10 <= number_people <= 24 and type_ticket == "Normal":
    transport = budged * 0.50
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= NORMAL:
        result = f"Yes! You have {real_budged - normal_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {normal_people - real_budged:.2f} leva."

elif 25 <= number_people <= 49 and type_ticket == "VIP":
    transport = budged * 0.40
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= IP:
        result = f"Yes! You have {real_budged - ip_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {ip_people - real_budged:.2f} leva."
elif 25 <= number_people <= 49 and type_ticket == "Normal":
    transport = budged * 0.40
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= NORMAL:
        result = f"Yes! You have {real_budged - normal_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {normal_people - real_budged:.2f} leva."

elif number_people >= 50 and type_ticket == "VIP":
    transport = budged * 0.25
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= IP:
        result = f"Yes! You have {real_budged - ip_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {ip_people - real_budged:.2f} leva."
elif number_people >= 50 and type_ticket == "Normal":
    transport = budged * 0.25
    real_budged = budged - transport
    budged_for_one = real_budged / number_people
    if budged_for_one >= NORMAL:
        result = f"Yes! You have {real_budged - normal_people:.2f} leva left."
    else:
        result = f"Not enough money! You need {normal_people - real_budged:.2f} leva."

print(result)
