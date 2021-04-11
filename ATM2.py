#registor
#- first name, last name and password
#generate user account

#login
#-account number and password


#bank operations

#Initalizing the system
import random

database = {} #dictionary

def init():

    isValidOptionSelected = False
    print('Welcome to bank Python')

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(registor())
        else:
            print("You have selected an invalid option")


def login():

    print("***** Login *****")


    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[2] == password):
                bankOperations(userDetails)

    print('Invalid account or password')
    login()

def registor():

    print("**** Registor ****")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create a password? \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, password ]

    print("Your account has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()
    
def bankOperations(user):

    print("Welcome %s %s" % ( user[0], user[1]) )

    from datetime import datetime

    now = datetime.now()
        
    print("now =", now)

    selectedOption = int(input("What would you like to do? (1) withdrawal (2) deposit (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        withdrawalOperation()

    elif(selectedOption == 2):
        depositOperation()

    elif(selectedOption == 3):
        login()

    elif(selectedOption == 4):
        exit()

    else:
        print('Invalid option selected')
        bankOperations(user)


def withdrawalOperation():
    print("**Withdrawal**")
    print('How much would you like to withdraw:')
    withdrawal = int(input('Please type in your response. \n'))
    print('Please take your cash')
    print("Your new balance is:")
    import random
    print(random.randrange(100,500))
    print("Back to the Main menu")
    login()
    
def depositOperation():
    print("**Deposit**")
    print("How much would you like to deposit?")
    deposit = int(input('Please make your deposit here \n'))
    print("Your current balance is:")
    import random
    print(random.randrange(1000,3000))
    print("Back to the Main menu")
    login()
        
def generationAccountNumber():

    return random.randrange(111111,999999)



#### ACTUAL BANKING SYSTEM ####

init()
