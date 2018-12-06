#Jared McMahon
#10/18
#password program

def menu():
    choice = 0
    while choice == 0:
        print ("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("choice one")
            username = get_username()
            password = get_password()
            choice = 0

        elif choice == 2:
            login = check_account(username, password)
            return password, username, login
        else:
            print("thts not a valid option")
            menu()

def get_password():
    print("""your password must start with a capital letter
and must contain at least 1 symbol
and must be at least 10 characters long""")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("your password didn't meet the requirements")
        get_password()

def get_username():
    print("""only contain numbers and letters
can only contain 10 characters
must contain at least 3 characters""")
    username = input("enter your user name")
    if username.isalnum() and len(username)<=10 and len(username)>=3:
        print("your user name is set")
        return username
    else:
        print("your user name didn't meet the requirements")
        get_username()

def check_account():
    username = username
    password = password
    enterusername=input("enter your user name")
    enterpassword=input("enter your password")
    if username == enterusername and password == enterpassword or enterusername =="admin":
        return True
    else:
        print("thats incorrect")
        menu()
    
def main():
    login = False
    password, username, login = menu()

    if True:
        print("you got in")
    else:
        print("access denied")

main()
