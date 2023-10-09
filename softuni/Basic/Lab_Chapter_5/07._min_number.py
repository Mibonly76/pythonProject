from sys import maxsize

command = input()
min_number = maxsize

while command != "Stop":
    command = int(command)
    if command < min_number:
        min_number = command
    command = input()

print(min_number)
