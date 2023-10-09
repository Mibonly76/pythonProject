string_input = input()

digits_string = ""
text_string = ""
symbols_string = ""


for element in string_input:

    if element.isdigit():
        digits_string += element
    elif element.isalpha():
        text_string += element
    else:
        symbols_string += element

print(digits_string)
print(text_string)
print(symbols_string)
