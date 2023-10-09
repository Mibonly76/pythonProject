import re

total_calories = 0
total_days = 0

incoming_data = input()
pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2,}\/\d{2,}\/\d{2,})\1(\d+)\1"
matches = re.findall(pattern, incoming_data)

for match in matches:
    total_calories += int(match[3])

total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
