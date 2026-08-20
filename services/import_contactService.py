from repositories.import_contactRepository import ImportContactRepository

class ImportContactService:
    def __init__(self, contact_book):
        self.import_contact_repository = ImportContactRepository(contact_book)

    def import_contact(self,file_name):
        return self.import_contact_repository.import_contact(file_name)
