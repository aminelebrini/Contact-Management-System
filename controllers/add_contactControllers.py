from services.add_contactService import AddContactService
from core.datavalidation import DataValidation

class AddContactController:
    def __init__(self, contact_book):
        self.addcontactservice = AddContactService(contact_book)
        self.data_validation = DataValidation()

    def addcontact(self,data):

        if(self.data_validation.validatefull_name(data["full_name"]) and 
           self.data_validation.validate_phone(data["phone"]) and 
           self.data_validation.validate_email(data["email"])
        ):
            return self.addcontactservice.addcontact(data)
        else:
            raise ValueError("data invalid !")