cipher_list = input().split(" ")

digit = []
new_word = ""
final_list = []

for cipher_word in cipher_list:
    digit = [element_digit for element_digit in cipher_word if element_digit.isdigit()]
    word = [element_word for element_word in cipher_word if element_word.isalpha()]

    digit_to_asci = chr(int("".join([item for item in digit])))
    if len(word) > 1:
        first_letter = word.pop(0)
        last_letter = word.pop(-1)
        word.append(first_letter)
        word.insert(0, last_letter)

    new_word = digit_to_asci + ("".join(word))
    final_list.append(new_word)


print(" ".join(final_list))
