accNumber = 123456
pinNumber = 1234
balance = 150000

userAccNumber = input("Enter Acc Number: ")
userPinNumber = input("Enter Pin Number: ")
if(userAccNumber.isnumeric() and userPinNumber.isnumeric()):

    if(accNumber == int(userAccNumber) and pinNumber == int(userPinNumber)):
        option = input("Enter a option 1. withdraw 2. check balance 3. deposit")
        if(option == "1" or option == "2" or option == "3"):
            if(option == "1"):
                withdrwaAmount = input("Enter amount to be withdraw: ")
                if(withdrwaAmount.isnumeric()):
                    withdrwaAmount = int(withdrwaAmount)
                    if(balance >= withdrwaAmount):
                        balance -= withdrwaAmount
                        print(f'Balance Amount: { balance }')
                    else:
                        print("In sufficient balance.")
                else:
                    print("Enterted invalid number.")
            elif(option == "2"):
                print(f"Balance Amount: { balance }")
            elif(option == "3"):
                depositAmount = input("Enter Amount to be deposit: ")
                balance += int(depositAmount)
                print(balance)
        else:
            print("You have choosen invalid option.")
    else:
        print("Enter valid Account number and Pin number.")
else:
    print("Enter only numbers.")

