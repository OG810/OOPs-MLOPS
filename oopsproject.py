class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False

    def menu(self):
        user_input = input(
            "Welcome to the chatbook!! How would you like to proceed?\n"
            "1. Press 1 to sign up\n"
            "2. Press 2 to sign in\n"
            "3. Press 3 to write a post\n"
            "4. Press 4 to message a friend\n"
            "5. Press any other key to exit\n"
        )
        print("You entered:", user_input)  # This will print the entered value

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

obj = chatbook()
obj.menu()

            







