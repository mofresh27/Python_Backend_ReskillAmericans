#AuthenticationSystem

import random
accountDataBase={}
depositDatabase={}
def welcome():

    validOptions = False
    print("Welcome to DMV Credit Union")
    while validOptions == False:
    
        haveAccount = int(input("Do you have an account with us: 1(yes) 2(no)\n"))

        if(haveAccount == 1):
            validOptions = True
            login()
        elif(haveAccount == 2 ):
            validOptions = True
            register()
        else:
            print("Invalid option, please select 1 for yes or 2 for no")
    

def login():
    print("Login")

    accountNumberFromUser = int(input("Account Number\n"))
    password = input("Password\n")


    for accountNumber, userDetails, in accountDataBase.items():
        if(accountNumber==accountNumberFromUser):
            if(userDetails[3]==password):
                bankOperations(userDetails)
    print ("Invalid account number or password, please try again")
    login()

def register():
    print("If you would like to be a part of the DMV family please register")
    email = input ("Email Address\n")
    first_name = input("First Name\n")
    last_name = input("Last or Surname\n")
    password = input("Create a new password\n")


    acountNumber = generateAccountNum()
    accountDataBase[acountNumber]= [first_name, last_name, email, password]

    print("Welcome to the DMV Family!")
    print("Your new account number is: %d"% acountNumber)
    deposit()



def bankOperations(user):

  
    print("Welcome %s %s" % (user[0], user[1]))
    option = int(input("How can we help you today? (1) deposit (2) withdraw (3) complaint (4) balance (5) logout (6) account number \n"))

    if (option == 1):
        deposit2()
    elif(option == 2):
        withdraw()
    elif(option == 3):
        complaint()
    elif(option == 4):
        balance()
    elif (option == 5):
        logout()
    elif (option == 6):
        logout()
    else:
        print("Invalid Option, please try again")
        bankOperations(user)


def logout():
    login()


def withdraw():
    verify_email = input("verify email\n")
    despositAmount = int(input("how much would you like to withdraw?\n"))
    depositDatabase[verify_email]-=despositAmount
    print(depositDatabase)
    bankOperations(verify_email)

def deposit2():
    print("Now that you are a part of the family, please make an inital depost:")
    verify_email = input("verify email\n")
    depositAmount = int(input("How much would you like to deposit?\n"))

    depositDatabase[verify_email]+=depositAmount
    print(depositDatabase)
    bankOperations(verify_email)

def deposit():
    print("Now that you are a part of the family, please make an inital depost:")
    verify_email = input("verify email\n")
    depositAmount = int(input("How much would you like to deposit?\n"))

    depositDatabase[verify_email]=depositAmount
    print(depositDatabase)
    bankOperations(verify_email)
    


def complaint():
    input("What would you like to report?\n")
    logout()
     

def balance():

    verify_email = input("verify email\n")
    print(depositDatabase)
    bankOperations(verify_email)
    

def generateAccountNum():
    return random.randrange(1111111111,9999999999)



### BANKING SYSTEM ####


welcome()


