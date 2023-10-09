class Email:
    def __init__(self, sender: str, receiver: str, content: str, is_send=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []
indexes = []

while True:
    input_string = input().split()

    if input_string[0] == "Stop":
        break
    # sender, receiver, content = input_string
    sender = input_string[0]
    receiver = input_string[1]
    content = input_string[2]

    email = Email(sender, receiver, content)
    emails.append(email)
indexes = [int(i) for i in input().split(", ")]

for index in indexes:
    #if 0 <= index < len(indexes):
    emails[index].send()
for email in emails:
    print(email.get_info())
