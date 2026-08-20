
class RemoveContactRepository:
    def __init__(self, contact_book):
        self.contact_book = contact_book

    def remove_contact(self, id):
            return self.contact_book.remove_contact(id)