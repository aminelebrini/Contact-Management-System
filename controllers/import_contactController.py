from services.import_contactService import ImportContactService

class ImportContactController:

    def __init__(self, contact_book):
        self.import_contact_service = ImportContactService(contact_book)

    def import_contacts(self,file_name):
        return self.import_contact_service.import_contact(file_name)