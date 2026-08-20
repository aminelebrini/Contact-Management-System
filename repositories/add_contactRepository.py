from models.Contact import Contact

class AddContactRepository:
    def __init__(self, contact_book):
        self.contact_book = contact_book

    def addcontact(self, data):
        new_contact = Contact(
            id = data["id"],
            full_name=data["full_name"],
            phone=data["phone"],
            email=data["email"]
        )

        new_contact_book = self.contact_book.add_contact(new_contact)

        if(new_contact_book):
            return new_contact_book
        else:
            return None
