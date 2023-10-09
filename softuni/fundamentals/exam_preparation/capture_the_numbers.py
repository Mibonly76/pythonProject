def contains_substring(raw_activation_key, command):
    substring = command[1]
    if substring in raw_activation_key:
        return f"{raw_activation_key} contains {substring}"
    return "Substring not found!"


def flipping(raw_activation_key, command):
    upper_lower = command[1]
    start_index = int(command[2])
    end_index = int(command[3])
    before_substring = raw_activation_key[:start_index]
    after_substring = raw_activation_key[end_index:]
    substring = raw_activation_key[start_index: end_index]
    if upper_lower == "Upper":
        substring = substring.upper()
    elif upper_lower == "Lower":
        substring = substring.lower()
    raw_activation_key = before_substring + substring + after_substring
    return raw_activation_key


def slicing(raw_activation_key, command):
    start_index = int(command[1])
    end_index = int(command[2])
    before_substring = raw_activation_key[:start_index]
    after_substring = raw_activation_key[end_index:]
    raw_activation_key = before_substring + after_substring
    return raw_activation_key


activation_key = input()
current_command = input()
while current_command != "Generate":
    current_command = current_command.split(">>>")
    action = current_command[0]
    if action == "Contains":
        print(contains_substring(activation_key, current_command))
    elif action == "Flip":
        activation_key = flipping(activation_key, current_command)
        print(activation_key)
    elif action == "Slice":
        activation_key = slicing(activation_key, current_command)
        print(activation_key)
    current_command = input()
print(f"Your activation key is: {activation_key}")
