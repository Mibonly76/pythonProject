import re

input_string = input()
destination_points = []

travel_points = 0
pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"

result = re.finditer(pattern, input_string)
if not result:
    pass
else:
    for element in result:
        element = element.group(2)
        travel_points += len(element)
        destination_points.append(element)

print(f"Destinations: {', '.join(destination_points)}\nTravel Points: {travel_points}")
