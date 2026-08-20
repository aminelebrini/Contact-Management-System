from services.remove_contactService import RemoveContactService
from core.datavalidation import DataValidation
class RemoveContactController:
    def __init__(self, contact_book):
        self.remove_contact_service = RemoveContactService(contact_book)
        self.data_validation = DataValidation()

    def remove_contact(self, id):
        if self.data_validation.validate_id(id):
            return self.remove_contact_service.remove_contact(id)
        else:
            raise ValueError("invalid data type !")
        