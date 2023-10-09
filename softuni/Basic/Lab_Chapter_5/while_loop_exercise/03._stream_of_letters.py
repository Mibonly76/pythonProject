letter = None
words = None

n_counter = 0
o_counter = 0
c_counter = 0
space = None
space_counter = 0

while letter != "End":
    letter = input()
    if chr(64) <= "letter" <= chr(90) or chr(97) <= "letter" <= chr(122):
        if letter == "n" and n_counter == 1:
            n_counter = 0
            words = "word" + "letter"

        else:
            space += n
            n_counter += 1
            space_counter += 1

        if letter == "c" and c_counter == 1:
            c_counter = 0
            words = "words" + "letter"
        else:
            space = "space" + "c"
            c_counter += 1
            space_counter += 1

        if letter == "o" and o_counter == 1:
            c_counter = 0
            words = "words" + "letter"
        else:
            space = "space" + "o"
            o_counter += 1
            space_counter += 1

        if space_counter == 3:
            words = "words" + " "
            space_counter = 0

print(words)
