class ContactBook:
    def __init__(self):
      self.contacts = []
      
    def add_contact(self, contact):
        self.contacts.append(contact)

    def modify_contact(self, contact):
        for i in self.contacts:
            if i.id == contact.id:
                i.full_name = contact.full_name
                i.phone = contact.phone
                i.email = contact.email
                return

    def display_contact(self):
        return self.contacts