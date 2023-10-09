phone_book = {}

while True:
    phone_contact = input()
    if "-" not in phone_contact:
        break
    contact, phone = phone_contact.split("-")
    phone_book[contact] = phone

for _ in range(int(phone_contact)):
    check_contact = input()
    if check_contact in phone_book.keys():
        print(f"{check_contact} -> {phone_book[check_contact]}")
    else:
        print(f"Contact {check_contact} does not exist.")
