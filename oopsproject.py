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
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            pass
        else:
            exit()
    def signup(self):
        email=input("Enter your email")
        passw=input("eneter your password")
        self.username=email
        self.password=passw
        print("u have signed up successfully !!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and  self.password=='':
            print("please sign up first by pressing 1")
        else:
            uname=input("Enter ur username/emai here ")
            passw=input("enetr ur passwrod here ")
            if self.username==uname and self.password==passw:
                print("u have signed up successfully !")
                self.loggedin=True
            else:
                print("give correct credentials")
        print("\n")
        self.menu()     
    def write_post(self):
        if self.loggedin:
            post=input("Rite ur post here ")
            print("post written successfully",post)
        else:
            print("please sign in forst by using 2")
        print("\n")
        self.menu()
        




obj = chatbook()
obj.menu()

            







