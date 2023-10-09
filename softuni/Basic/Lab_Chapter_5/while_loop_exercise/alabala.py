import string
c_counter = 0
o_counter = 0
n_counter = 0
word = ""
letter_counter = 0
command = input()
while True:
    if command not in string.ascii_letters and command != "End":
        command = input()
        continue
    if command == "c" and c_counter == 0:
        c_counter += 1
        command = input()
        continue
    if command == "o" and o_counter == 0:
        o_counter += 1
        command = input()
        continue
    if command == "n" and n_counter == 0:
        n_counter += 1
        command = input()
        continue
    if c_counter > 0 and o_counter > 0 and n_counter > 0:
        word = word + " "
        c_counter = 0
        n_counter = 0
        o_counter = 0
        letter_counter = 0
        if command == "End":
            break
    letter_counter += 1
    word += command
    command = input()
    if command == "End":
        break

if letter_counter == 0:
    print(f"{word}")
else:
    word = word[:-letter_counter]
    print(f"{word}")
