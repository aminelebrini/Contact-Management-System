from repositories.add_contactRepository import AddContactRepository

class AddContactService:
    def __init__(self):
        self.addcontactrepository = AddContactRepository()

    def addcontact(self, data):
        return self.addcontactrepository.addcontact(data)