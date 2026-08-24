from models.Contact import Contact

class ContactBook:
    def __init__(self):
      self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        with open("data/contacts.txt", "a", encoding="utf-8") as file:
            for contact in self.contacts:
                file.write(
                    f"{contact.full_name},"
                    f"{contact.phone},"
                    f"{contact.email}\n"
                )

    def modify_contact(self, contact):
        for i in self.contacts:
            if i.id == contact.id:
                i.full_name = contact.full_name
                i.phone = contact.phone
                i.email = contact.email
                return

    def remove_contact(self, full_name):
        with open("data/contacts.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        remaining = [line for line in lines if line.strip() and line.split(",")[0] != full_name]

        with open("data/contacts.txt", "w", encoding="utf-8") as file:
            file.writelines(remaining)

    def display_contact(self):
        contacts = []
        with open("data/contacts.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    contacts.append(Contact(parts[0], parts[1], parts[2]))
        return contacts