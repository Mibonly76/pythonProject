def abjuration(spell):
    return spell.upper()


def necromancy(spell):
    return spell.lower()


def illusion(spell, index, letter):
    if 0 <= index < len(spell):
        spell = spell[:index] + letter + spell[index + 1:]
        return spell, "Done!"
    else:
        return spell, "The spell was too weak."


def divination(spell, first_substring, second_substring):
    if first_substring in spell:
        spell = spell.replace(first_substring, second_substring)
        print(spell)
    return spell


def alteration(spell, substring):
    if substring in spell:
        spell = spell.replace(substring, '')
        print(spell)
    return spell


spell = input()

while True:
    command = input()
    if command == "Abracadabra":
        break

    tokens = command.split()
    action = tokens[0]

    if action == "Abjuration":
        spell = abjuration(spell)
        print(spell)
    elif action == "Necromancy":
        spell = necromancy(spell)
        print(spell)
    elif action == "Illusion":
        index = int(tokens[1])
        letter = tokens[2]
        spell, result = illusion(spell, index, letter)
        print(result)
    elif action == "Divination":
        first_substring = tokens[1]
        second_substring = tokens[2]
        spell = divination(spell, first_substring, second_substring)
    elif action == "Alteration":
        substring = tokens[1]
        spell = alteration(spell, substring)

    else:
        print("The spell did not work!")
