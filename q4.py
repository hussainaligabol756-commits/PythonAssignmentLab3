balance=50000
while(True):
    print("*****WELCOME TO ATM SYSTEM*****")
    print("ATM menu:\n"+"1.Check Balance\n"+"2.Deposit\n"+"3.withdraw\n"+"4.exit")
    choice=int(input("Enter your choice: "))
    if(choice == 1):
        print("The current balance: ",balance)
    elif(choice==2):
        deposit=int(input("Enter your deposit amount: "))  
        balance+=deposit
        print("The current balance: ",balance)
    elif(choice==3):
        withdraw=int(input("Enter your withdraw amount: "))
        if(balance > withdraw):
            balance-=withdraw
            print("The current balance: ",balance)
        else:
            print("Insufficient balance")
    elif(choice==4):
        break