from controllers.add_contactControllers import AddContactController

if __name__ == "__main__":

    addcon = AddContactController()

    id = ""
    full_name = ""
    phone = ""
    email = ""

    print("Welcome to Your Contact Space")
    print("You Can Shoose One of This choises: ")
    
    while True:

        print("""
            1 - Add Contact
            2 - Modify Contact
            3 - Remove Contact
            4 - Search for Contact
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
                addcon.addcontact(data)

            case 2:
                print("Modify Contact")

            case 3:
                print("Remove Contact")

            case 4:
                print("Search Contact")

            case 5:
                print("Import Contact")

            case 0:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice")