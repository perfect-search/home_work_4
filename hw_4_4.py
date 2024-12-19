
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def replace_phone(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Phone replaced."


def get_contact_user(args, contacts):
    name = args
    return contacts[name[0]]


def get_all_numbers(contacts):
    list_numbers = []
    for value in contacts.values():
        list_numbers.append(value)

    return list_numbers

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(replace_phone(args, contacts))
        elif command == "phone":
            print(get_contact_user(args, contacts))
        elif command == "all":
            print(get_all_numbers(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
