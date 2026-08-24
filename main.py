from models.ContactBook import ContactBook
from controllers.add_contactControllers import AddContactController
from controllers.display_contactController import DisplayContactController
from controllers.remove_contactController import RemoveContactController
from controllers.import_contactController import ImportContactController
if __name__ == "__main__":

    contact_book = ContactBook()

    addcontact_controller = AddContactController(contact_book)
    displaycontact_controller = DisplayContactController(contact_book)
    removecontact_controller = RemoveContactController(contact_book)
    importcontact_controller = ImportContactController(contact_book)
    

    full_name = ""
    phone = ""
    email = ""

    print("Welcome to Your Contact Space")
    print("You Can Shoose One of This choises: ")
    
    while True:

        print("""
            1 - Add Contact
            2 - Display Contacts
            3 - Remove Contact
            4 - Import Contact from CSV
            0 - Exit
            """)

        n = int(input("Enter Your Choice: "))

        match n:
            case 1:
    
                full_name = str(input("enter the fullname : "))
                phone = str(input("enter the phone number : "))
                email = str(input("enter the email : "))
                data = {
                            "full_name": full_name,
                            "phone" : phone,
                            "email" : email
                                   }
                addcontact_controller.addcontact(data)

            case 2:
                print("These are your registered contacts: ")
                contacts = displaycontact_controller.get_contact_data()
                if contacts:
                    for contact in contacts:
                        print(f"Name: {contact.full_name}, Phone: {contact.phone}, Email: {contact.email}")
                else:
                    print("No contacts found.")

            case 3:
                contacts = displaycontact_controller.get_contact_data()
                if contacts:
                    for contact in contacts:
                        print(f"Name: {contact.full_name}, Phone: {contact.phone}, Email: {contact.email}")
                else:
                    print("No contacts found.")

                id = int(input("please inter the id for contact : "))

                removecontact_controller.remove_contact(full_name)

            case 4:
                filename = input("Enter the file name: ")
                try:
                    importcontact_controller.import_contacts(filename)
                    print("Contacts imported successfully.")

                except FileNotFoundError:
                    print("File not found.")

                except ValueError:
                    print("Invalid contact data.")
            case 0:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice")