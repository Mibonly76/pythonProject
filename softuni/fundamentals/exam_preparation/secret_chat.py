def insert_space(message, command_index):
    command_index = int(command_index)
    message = message[0:command_index] + " " + message[command_index:]
    print(message)
    return message


def reverse(message, command_substring):
    if command_substring in message:
        message = message.replace(substring, "", 1)
        message = message + substring[::-1]
        print(message)

    else:
        print("error")
    return message


def change_all(message, command_string, command_replacement):
    message = message.replace(command_string, command_replacement)
    print(message)
    return message


concealed_message = input()

while True:
    given_command = input()

    if given_command.startswith("Reveal"):
        print(f"You have a new text message: {concealed_message}")
        break

    elif given_command.startswith("InsertSpace"):
        command, index = given_command.split(":|:")
        concealed_message = insert_space(concealed_message, index)

    elif given_command.startswith("Reverse"):
        command, substring = given_command.split(":|:")
        concealed_message = reverse(concealed_message, substring)

    else:
        command, substring, replacement = given_command.split(":|:")
        concealed_message = change_all(concealed_message, substring, replacement)
