from models.Contact import Contact

class ImportContactRepository:
    def __init__(self, contact_book):
        self.contact_book = contact_book

    def import_contact(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().strip("(),")

                if not line or "=" in line or "[" in line or "]" in line:
                    continue

                data = line.split(",")
                if len(data) != 4:
                    continue

                contact = Contact(
                    id=int(data[0].strip()),
                    full_name=data[1].strip().strip('"'),
                    phone=data[2].strip().strip('"'),
                    email=data[3].strip().strip('"')
                )
                self.contact_book.add_contact(contact)
        