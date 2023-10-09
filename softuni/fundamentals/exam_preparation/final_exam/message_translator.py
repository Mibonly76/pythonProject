import re


def is_valid_string(input_string):
    pattern = r"!(?P<command>[A-Z][a-zA-Z]{2,})!:\[(?P<string>[A-Za-z]{8,})\]"
    match = re.match(pattern, input_string)
    return match


def translate_string(input_string):
    match = is_valid_string(input_string)
    if match:
        command = match.group("command")
        string_to_translate = match.group("string")
        translated_string = " ".join(str(ord(char)) for char in string_to_translate)
        return f"{command}: {translated_string}"
    else:
        return "The message is invalid"


n = int(input())
for _ in range(n):
    input_string = input()
    result = translate_string(input_string)
    print(result)
