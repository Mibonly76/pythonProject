from sys import maxsize

command = input()
max_number = -maxsize

while command != "Stop":
    command = int(command)
    if command > max_number:
        max_number = command
    command = input()

print(max_number)
