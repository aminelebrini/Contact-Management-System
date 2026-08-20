from repositories.display_contactRepository import DisplayContactRepository

class DisplayContactService:
    def __init__(self, contact_book):
        self.contact_repository = DisplayContactRepository(contact_book)

    def get_contacts(self):
        return self.contact_repository.get_contacts()