number_of_electrons = int(input())

shel_number = 1
the_shell_electron_value = 0
final_sequence_list = []

while True:
    the_shell_electron_value = shel_number**2 * 2
    if (number_of_electrons - the_shell_electron_value) > 0:
        final_sequence_list.append(the_shell_electron_value)
        number_of_electrons -= the_shell_electron_value
        shel_number += 1
    else:
        final_sequence_list.append(number_of_electrons)
        break


print(final_sequence_list)
