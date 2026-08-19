from models.Contact import Contact
from models.ContactBook import ContactBook

class AddContactRepository:
    def __init__(self):
        pass

    def addcontact(self, data):
        new_contact = Contact(
            id = data["id"],
            full_name=data["full_name"],
            phone=data["phone"],
            email=data["email"]
        )

        # contact_book = ContactBook.add_contact(new_contact)

        # if(contact_book):
        #     return contact_book
        # else:
        #     return None
