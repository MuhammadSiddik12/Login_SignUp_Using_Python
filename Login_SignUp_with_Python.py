print("\nWelcome To My Website ")
def SignUp_login(welcome):
    if welcome == "1":
        name=input('\nEnter Your Name: ')
        username  = input("\nEnter a username:")
        phone=input('\nEnter Your Phone number: ')
        password  = input("\nEnter a password:")
        password1 = input("\nEnter a Confirm password:")
        if password == password1:
            try:
                file = open(username+".txt", "r")
                data   = file.readline().split(':')
                if username in data[1] and password in data[-1]:
                    print("\nUser already found")
                    file.close()
            except:
                file = open(username+".txt", "w")
                file.write(name+':'+username+':'+phone+":"+password)
                file.close()
                print('\nYou Successfully SignUp !')
        else: print("\nPasswords do NOT match !")
    elif welcome == "2":
        login1 = input("\nUserName : ")
        login2 = input("\nPassWord : ")
        try:
            file = open(login1+".txt", "r")
            data   = file.readline().split(':')
            if login1 in data[1] and login2 in data[-1]:
                print("\nWelcome")
                file.close()
        except:
            print('\nuser not found') if FileNotFoundError else None
welcome = input("\n1. SignUp \n2. Login \n\n")
SignUp_login(welcome)