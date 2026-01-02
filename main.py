import authentication
print("Welcome to Checkly!!")
print("********************\n")

def main_dashboard():
    print("waiting")

#This function is for inital start of CLI-APP user needs to login to move further
def landing():
    print("Please Login to continue to main dashboard!")
    print("1.Login to checkly \n2.Create an New account \n3.Close the program")
    choice_login = int(input("Enter your Preference: "))
    match(choice_login):
        case(1):
            print("---redirecting to login page---")
            if(authentication.login()):
                main_dashboard()
            else:
                print("User credentials  are invaild!")
                print("retry or close the program")
                landing()
        case(2):
            print("---redirecting to Account Creation page---")
            authentication.NewUser()
        case(3):
            print("Closing the program safely!!")

landing()