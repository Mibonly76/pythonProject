input_text = input()
output_text = [letter for letter in input_text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(output_text))
