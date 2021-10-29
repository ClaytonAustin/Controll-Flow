#Developer:Clayton Austin
#date: 10/11/21
#Program: ATM Bank Transaction

'''
This program simulates an ATM utilizing If, Elif, & Else statements
Nesting our if statements and introduce/refresh our comparison & logical Operators
'''

print("Welcome to Cash-R-Us Bank. \n\nLet's take a moment to set up your account. \n")

#Set up account by asking users by asking for there fist and last names using variables
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("\nWelcome To Cash-R-Us",firstName,lastName + ", We Will Now Set Up A Security Pin On Your Account. \n")

#set up a PIN (Personal Identification Number)

pin = input("please chose a four-digit security pin: ")

print("\nThank you", firstName + ",we see that you set your pin to",pin)

print("\nWould You Like To Make A Transaction Through Our ATM")

atm = input("Yes or No: ").upper()

if atm == "YES":
    print("\n****************************************************************************\n")

# This part of the program will be asking users to complete a transaction through the ATM.
    print("Please Insert Card Now\n")
    print("Welcome to Cash-R-Us ATM",firstName,lastName,"\n")
    userPIN = input("What Is Your PIN Number: ")

    if pin == userPIN:
        balance = 674
        print("\nYour Balance: $" + str(balance))

        # Ask Users what type of transaction they want - Withdrawal - Deposit
        typeOfTransaction = input("\nWould you like to make a Withdrawal or Deposit\nW = withdrawal Or D = Deposit B= Balance: ").lower()
        if typeOfTransaction == "w":
            withdrawalAmount = int(input("Enter amount of withdrawal: "))
            balance = balance - withdrawalAmount
            print("Your new balance is: $" + str(balance))
            
            
        
        elif typeOfTransaction == "d":
            depositAmount = int(input("Enter amount of your deposit: "))
            balance = balance + depositAmount
            print("your new balance is: $" + str(balance))


        else:
            print("your current balance is: $" + str(balance))
        
        

    else:print("\nSorry",firstName,lastName,"Your pin is incorrect")

else:
    print("\nHave a wonderful day",firstName,lastName + ", please come back and visit soon.")























