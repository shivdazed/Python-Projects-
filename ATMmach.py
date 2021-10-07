acct_bal=10000
pin=160293
att = 2
att_p = int(input("Please enter your ATM pin:"))
if att_p == pin:
    option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")
    while option != '4':
        if option == '1':
            print("Current Account Balance :",acct_bal)
            ret = input("If you wish to continue press Y and N to Exit")
            if ret == 'Y':
                option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")                
            elif ret == 'N':
                break
        elif option == '2':
            credit = int(input("Enter the amount to be credited into your account: "))
            print("Current Account Balance is:",acct_bal+credit)
            ret = input("If you wish to continue press Y or N to Exit:")
            if ret == 'Y':
                option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")
            elif ret == 'N':
                break
        elif option == '3':
            debit = int(input("Enter the amount to be debited into your account: "))
            print("Current Account Balance is:",acct_bal-debit)
            ret = input("If you wish to continue press Y or N to Exit:")
            if ret == 'Y':
                option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")
            elif ret == 'N':
                break
else:
    while (att >=1):
        if att_p == pin:
            option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")
            while option != '4':
                if option == '1':
                    print("Current Account Balance :",acct_bal)
                    ret = input("If you wish to continue press Y and N to Exit")
                    if ret == 'Y':
                        option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")                
                    elif ret == 'N':
                        break
                elif option == '2':
                    credit = int(input("Enter the amount to be credited into your account: "))
                    print("Current Account Balance is:",acct_bal+credit)
                    ret = input("If you wish to continue press Y or N to Exit:")
                    if ret == 'Y':
                        option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")
                    elif ret == 'N':
                        break
                elif option == '3':
                    debit = int(input("Enter the amount to be debited into your account: "))
                    print("Current Account Balance is:",acct_bal-debit)
                    ret = input("If you wish to continue press Y or N to Exit:")
                    if ret == 'Y':
                        option = input("Choose a number beside the option \n1--Account Balance \n2--Credit\n3--Debit\n4--Exit\n")
                    elif ret == 'N':
                        break
        elif att_p != pin:
            while(att >=1 and att_p !=pin):
                att-=1
                print("You have",att+1,"more attempts")
                att_p = int(input("Re-Enter Your ATM pin:"))
            if att == 0:
                print("Your card has been blocked\n Please contact your bank branch for further details.")
                break
        else:
            att_p=int(input("Invalid Input, Please Re-enter Your Pin"))
            







