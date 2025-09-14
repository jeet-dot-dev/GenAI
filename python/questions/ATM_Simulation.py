# acounts dictionary 
acounts = {
    "1011526982" : 5000,
    "1011726982" : 9000,
    "1011523982" : 5000,
    "1011526922" : 2000,
    "1011926982" : 5000,
    
}


def addBalance(account_number,amount):
    acounts[account_number]+=amount
    print(f"${amount} is depositd on yout account xxxxxxx{account_number[-4]}")
    showBalance(account_number)
    

def removeBalance(account_number,amount):
    if amount>acounts[account_number] :
        print("Sorry ! Unsufficient amount ")
        return

    acounts[account_number]-=amount
    print(f"${amount} is withdrawn from yout account xxxxxxx{account_number[-2]}")
    showBalance(account_number)

def showBalance(account_number):
    print(f"Your current balance is : ${acounts[account_number]}")

def atm():
    account_number = input("Enter your 10 digit accout number plz : ")
    if len(account_number)!=10 :
        return "Plz Enter a valid account number!"
    while True :
        action = input("Choose action (balance/deposit/withdraw/exit) : ").lower()
        match action :
            case "balance":
                showBalance(account_number)
            case "deposit":
                amount = int(input("Enter the amount you want to deposit : "))    
                addBalance(account_number,amount)
            case "withdraw":
                amount = int(input("Enter the amount you want to withdraw : "))    
                removeBalance(account_number,amount)    
            case "exit":
                print("Thanks for coming . Have a nice day")
                return    
            case _:
                print("Unknown command")
            

atm()            