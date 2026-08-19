class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)

    def modify_contact(self, contact):
        for id in self.contacts:
            if(self.contacts[id] == contact[id]):
                self.contacts = contact

    def display_contact(self):
        return self.contacts