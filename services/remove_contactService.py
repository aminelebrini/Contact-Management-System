from repositories.remove_contactRepository import RemoveContactRepository

class RemoveContactService:
    def __init__(self, contact_book):
        self.remove_contact_repository = RemoveContactRepository(contact_book)

    def remove_contact(self, full_name):
            return self.remove_contact_repository.remove_contact(full_name)