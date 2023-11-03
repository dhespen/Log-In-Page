username = "Admin"
password = "1234"
contFull = "Yes"

print("Username = Admin\nPassword = 1234")
while contFull == "Yes":

    userIn = input("Username: ")
    passIn = input("Password: ")

    if userIn == username and passIn == password:

        userChange = input("Would you like to change your username? ")

        if userChange == "Yes":

            username = input("New Username: ")

            print("Username successfully changed\n")

            passChange = input("Would you like to change your password? ")

            if passChange == "Yes":

                password = input("New Password: ")

                print("Password successfully changed\n\n")

        else:
            passChange = input("Would you like to change your password? ")

            if passChange == "Yes":
                password = input("New Password: ")

                print("Password successfully changed\n\n")


    cont = input("Would you like to log back out (Y) or shut down (N)? ")

    if cont == "Y":
        contFull = "Yes"

    else:
        exit()
