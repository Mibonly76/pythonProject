message = input()
command = input().split("|")

while "Decode" != command[0]:
    if command[0] == "Move":
        num = int(command[1])
        message = message[num:] + message[:num]
    elif command[0] == "Insert":
        index = int(command[1])
        value = str(command[2])
        message = message[:index] + value + message[index:]
    elif command[0] == "ChangeAll":
        old = str(command[1])
        new = str(command[2])
        message = message.replace(old, new)

    command = input().split("|")

print(f"The decrypted message is: {message}")
