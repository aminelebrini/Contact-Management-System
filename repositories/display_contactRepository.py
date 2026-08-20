from models.ContactBook import ContactBook

class DisplayContactRepository:
    def __init__(self, contact_book):
        self.contact_book = contact_book

    def get_contacts(self):
        return self.contact_book.display_contact()