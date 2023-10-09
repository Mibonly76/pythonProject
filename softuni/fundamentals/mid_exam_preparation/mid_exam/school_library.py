def add_book(my_shelf, book):
    if book not in my_shelf:
        my_shelf.insert(0, book)
    return my_shelf


def take_book(my_shelf, book):
    if book in my_shelf:
        my_shelf.remove(book)
    return my_shelf


def swap_books(my_shelf, first_book, second_book):
    if first_book in my_shelf and second_book in my_shelf:
        index_first_book = my_shelf.index(first_book)
        index_second_book = my_shelf.index(second_book)
        my_shelf[index_first_book], my_shelf[index_second_book] = \
            my_shelf[index_second_book], my_shelf[index_first_book]
    return my_shelf


def insert_book(my_shelf, book):
    if book not in my_shelf:
        my_shelf.append(book)
    return my_shelf


def check_book(my_shelf, element):
    if 0 <= element < len(my_shelf):
        print(my_shelf[element])


shelf = input().split("&")
command = input()

while command != "Done":
    instruction_list = command.split(" | ")
    action = instruction_list[0]
    book_name = instruction_list[1]

    if action == "Add Book":
        shelf = add_book(shelf, book_name)
    elif action == "Take Book":
        shelf = take_book(shelf, book_name)
    elif action == "Swap Books":
        book1 = instruction_list[1]
        book2 = instruction_list[2]
        shelf = swap_books(shelf, book1, book2)
    elif action == "Insert Book":
        shelf = insert_book(shelf, book_name)
    elif action == "Check Book":
        index = int(book_name)
        check_book(shelf, index)

    command = input()

print(", ".join(shelf))
