from services.display_contactService import DisplayContactService

class DisplayContactController:

    def __init__(self, contact_book):
        self.contact_service = DisplayContactService(contact_book)

    def get_contact_data(self):
        return self.contact_service.get_contacts()