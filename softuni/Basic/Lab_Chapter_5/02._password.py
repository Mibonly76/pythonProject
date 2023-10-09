username = input()
user_password = input()
password = input()

while password != user_password:
    password = input()

print(f"Welcome {username}!")
