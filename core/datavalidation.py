class DataValidation:
    def __init__(self):
        pass

    def validatefull_name(self,full_name):
        for char in full_name:
            if(char.isdigit()):
                return False
            else:
                continue
        return True

    def validate_phone(self,phone):
        if phone.isdigit() and len(phone) == 10:
            return True

        return False

    def validate_email(self,email):
        if "@" not in email:
            return False
        username = email.split("@")[0]
        domaine = email.split("@")[1]
        if(username.isdigit() and domaine.isdigit()):
            return False
        return True

                        