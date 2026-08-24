from services.remove_contactService import RemoveContactService
from core.datavalidation import DataValidation
class RemoveContactController:
    def __init__(self, contact_book):
        self.remove_contact_service = RemoveContactService(contact_book)
        self.data_validation = DataValidation()

    def remove_contact(self, full_name):
        if self.data_validation.validatefull_name(full_name):
            return self.remove_contact_service.remove_contact(full_name)
        else:
            raise ValueError("invalid data type !")
        