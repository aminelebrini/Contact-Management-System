def load_contacts():
    contacts = []

    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                if len(data) != 3:
                    continue

                contact = {
                    "name": data[0],
                    "phone": data[1],
                    "email": data[2]
                }

                contacts.append(contact)

    except FileNotFoundError:
        pass

    return contacts


def save_contacts(contacts):
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(
                f"{contact['name']},"
                f"{contact['phone']},"
                f"{contact['email']}\n"
            )


def add_contact(contacts):
    print("\n--- Add Contact ---")

    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact added successfully.")


def display_contacts(contacts):
    print("\n--- Registered Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. "
            f"Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )


def remove_contact(contacts):
    print("\n--- Remove Contact ---")

    if not contacts:
        print("No contacts found.")
        return

    display_contacts(contacts)

    try:
        choice = int(input("Enter the contact number to remove: "))

        if choice < 1 or choice > len(contacts):
            print("Invalid contact number.")
            return

        removed_contact = contacts.pop(choice - 1)

        save_contacts(contacts)

        print(
            f"Contact '{removed_contact['name']}' "
            "removed successfully."
        )

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":

    contacts = load_contacts()

    print("Welcome to Your Contact Space")

    while True:

        print("""
        1 - Add Contact
        2 - Display Contacts
        3 - Remove Contact
        0 - Exit
        """)

        try:
            choice = int(input("Enter Your Choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:

            case 1:
                add_contact(contacts)

            case 2:
                display_contacts(contacts)

            case 3:
                remove_contact(contacts)

            case 0:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice.")