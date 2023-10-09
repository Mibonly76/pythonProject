resources_dict = {}

while True:
    resource = input()
    if resource == "stop":
        break
    if resource not in resources_dict.keys():
        resources_dict[resource] = 0
    quantity = int(input())
    resources_dict[resource] += quantity

for key, value in resources_dict.items():
    print(f"{key} -> {value}")
