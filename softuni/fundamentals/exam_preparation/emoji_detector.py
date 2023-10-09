import re

coolness_dict = {}
elemetns_lists = []
emodji_coolness = 0
cool_threshold = 1
number_of_emojes = 0
incoming_data = input()
pattern1 = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
patern2 = r"\d"
matches = re.findall(pattern1, incoming_data)
digits_found = re.findall(patern2, incoming_data)

for digit in digits_found:
    cool_threshold *= int(digit)

for match in matches:
    number_of_emojes += 1
    word_from_list = match[1]
    for element in word_from_list:
        emodji_coolness += ord(element)
    if emodji_coolness > cool_threshold:
        elemetns_lists.append(match[0] + match[1] + match[0])
        emodji_coolness = 0

print(f"Cool threshold: {cool_threshold}")
print(f"{number_of_emojes} emojis found in the text. The cool ones are:")
for item_in_elemen in elemetns_lists:
    print(item_in_elemen)
