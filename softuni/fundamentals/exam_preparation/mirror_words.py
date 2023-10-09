import re

incoming_data = input()
pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
matches = re.findall(pattern, incoming_data)
found_palindromes = []
for match in matches:
    if match[1] == match[2][::-1]:
        found_palindromes.append(f"{match[1]} <=> {match[2]}")
if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if not found_palindromes:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(found_palindromes))
    