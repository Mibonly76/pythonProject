total_tickets = 0
total_counter_student_tickets = 0
total_counter_standard_tickets = 0
total_counter_kid_tickets = 0
total_tickets_for_all = 0
total_places = 0


while True:
    name = input()
    if name == "Finish":
        break
    free_places = int(input())
    total_places += free_places
    counter_student_tickets = 0
    counter_standard_tickets = 0
    counter_kid_tickets = 0
    sum_of_tickets = 0
    for _ in range(free_places):
        type_of_ticket = input()
        if type_of_ticket == "End" or sum_of_tickets > free_places:
            break
        if type_of_ticket == "student":
            counter_student_tickets += 1
            total_counter_student_tickets += 1
        elif type_of_ticket == "standard":
            counter_standard_tickets += 1
            total_counter_standard_tickets += 1
        elif type_of_ticket == "kid":
            counter_kid_tickets += 1
            total_counter_kid_tickets += 1
        sum_of_tickets = counter_standard_tickets + counter_kid_tickets + counter_student_tickets
        total_tickets += sum_of_tickets
    print(f"{name} - {sum_of_tickets / free_places * 100:.2f}% full.")

total_tickets_for_all = total_counter_student_tickets\
                        + total_counter_standard_tickets\
                        + total_counter_kid_tickets
print(f"Total tickets: {total_tickets_for_all}")
print(f"{total_counter_student_tickets / total_tickets_for_all * 100:.2f}% student tickets.")
print(f"{total_counter_standard_tickets / total_tickets_for_all * 100:.2f}% standard tickets.")
print(f"{total_counter_kid_tickets / total_tickets_for_all * 100:.2f}% kids tickets.")
