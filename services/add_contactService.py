from repositories.add_contactRepository import AddContactRepository

class AddContactService:
    def __init__(self, contact_book):
        self.addcontactrepository = AddContactRepository(contact_book)

    def addcontact(self, data):
        return self.addcontactrepository.addcontact(data)