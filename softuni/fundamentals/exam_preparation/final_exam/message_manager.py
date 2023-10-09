def manage_messages(capacity):
    messages = {}

    while True:
        command = input()
        if command == "Statistics":
            break

        tokens = command.split("=")
        action = tokens[0]

        if action == "Add":
            username, sent, received = tokens[1], int(tokens[2]), int(tokens[3])
            if username not in messages:
                messages[username] = {"sent": sent, "received": received}

        elif action == "Message":
            sender, receiver = tokens[1], tokens[2]
            if sender in messages and receiver in messages:
                messages[sender]["sent"] += 1
                messages[receiver]["received"] += 1

                if messages[sender]["sent"] + messages[sender]["received"] >= capacity:
                    print(f"{sender} reached the capacity!")
                    del messages[sender]
                if messages[receiver]["sent"] + messages[receiver]["received"] >= capacity:
                    print(f"{receiver} reached the capacity!")
                    del messages[receiver]

        elif action == "Empty":
            username = tokens[1]
            if username == "All":
                messages.clear()
            elif username in messages:
                del messages[username]

    print(f"Users count: {len(messages)}")

    for username, data in messages.items():
        total_messages = data["sent"] + data["received"]
        print(f"{username} - {total_messages}")


# Example usage:
capacity = int(input())
manage_messages(capacity)
