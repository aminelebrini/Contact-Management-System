from models.ContactBook import ContactBook
from controllers.add_contactControllers import AddContactController
from controllers.display_contactController import DisplayContactController
from controllers.remove_contactController import RemoveContactController

if __name__ == "__main__":

    contact_book = ContactBook()

    addcontact_controller = AddContactController(contact_book)
    displaycontact_controller = DisplayContactController(contact_book)
    removecontact_controller = RemoveContactController(contact_book)
    

    id = ""
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
            5 - Import Contact from CSV
            0 - Exit
            """)

        n = int(input("Enter Your Choice: "))

        match n:
            case 1:
                id = int(input("enter the contact id : "))
                full_name = str(input("enter the fullname : "))
                phone = str(input("enter the phone number : "))
                email = str(input("enter the email : "))
                data = {
                            "id" : id,
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
                        print(f"ID: {contact.id}, Name: {contact.full_name}, Phone: {contact.phone}, Email: {contact.email}")
                else:
                    print("No contacts found.")

            case 3:
                contacts = displaycontact_controller.get_contact_data()
                if contacts:
                    for contact in contacts:
                        print(f"ID: {contact.id}, Name: {contact.full_name}, Phone: {contact.phone}, Email: {contact.email}")
                else:
                    print("No contacts found.")

                id = int(input("please inter the id for contact : "))

                removecontact_controller.remove_contact(id)

            case 4:
                print("Import Contact")

            case 0:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice")