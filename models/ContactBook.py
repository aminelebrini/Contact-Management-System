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

    def remove_contact(self, id):
        for i in self.contacts:
            if i.id == id:
                self.contacts.remove(i)

        return self.contacts

    def display_contact(self):
        