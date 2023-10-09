parking_list = {}

input_validation_number = int(input())


for _ in range(input_validation_number):
    input_command = input().split()
    command = input_command[0]
    name = input_command[1]
    if command == "register":
        license_plate = input_command[2]
        if name not in parking_list:
            parking_list[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister":
        if name in parking_list:
            del parking_list[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")
for name, plate in parking_list.items():
    print(f"{name} => {plate}")
