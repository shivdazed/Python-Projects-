s = {'south indian':["1.idliplate-Rs40",'2.Dosa-Rs35','3.vada-Rs40'],
     'Chinese':['1.Soup-Rs25','2.Noodles-Rs65','3.Momos-Rs40'],
     'Maharashtrian':['1.Ussal-Rs25','2.Bhakri-Rs10','3.Puranpoli-Rs8'],
     'Punjabi':['1.CholeBhature-Rs50','2.Roti-Rs10','3.DalMakhni-Rs95']}
c = int(input("Enter your choice of cuisine.Press 1 -South Indian,2 -Chinese,3 -Maharashtrian,4 -Punjabi"))
if c == 1:
    for i in s['south indian']:
        print(i)

    s_c = int(input("Enter your choice in South Indian:"))
    if s_c == 1:
        otp = 1602
        otp_att = int(input("You have chosen idli plate\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
    elif s_c == 2:
        otp = 1603
        otp_att = int(input("You have chosen Dosa\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
    elif s_c == 3:
        otp = 1604
        otp_att = int(input("You have chosen Vada\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")

elif c == 2:
    for i in s['Chinese']:
        print(i)
    s_c = int(input("Enter your choice in Chinese:"))
    if s_c == 1:
        otp = 1702
        otp_att = int(input("\nYou have chosen Soup\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
    elif s_c == 2:
        otp = 1703
        otp_att = int(input("You have chosen Noodles\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
    elif s_c == 3:
        otp = 1704
        otp_att = int(input("You have chosen Momos\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
  
elif c == 3:
    for i in s['Maharashtrian']:
        print(i)
    s_c = int(input("Enter your choice in Maharashtrian:"))
    if s_c == 1:
        otp = 1802
        otp_att = int(input("\nYou have chosen Ussal\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
    elif s_c == 2:
        otp = 1803
        otp_att = int(input("You have chosen Bhakri\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("Please make the payment through your waiter.")
    elif s_c == 3:
        otp = 1804
        otp_att = int(input("You have chosen Puranpoli\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("Smile, your order is being prepared!")
        else:
            print("Please make the payment through your waiter.")

elif c == 4:
    for i in s['Punjabi']:
        print(i)
    s_c = int(input("Enter your choice in Punjabi:"))
    if s_c == 1:
        otp = 1902
        otp_att = int(input("\nYou have chosen CholeBhature\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("\nPlease make the payment through your waiter.")
    elif s_c == 2:
        otp = 1903
        otp_att = int(input("\nYou have chosen Roti\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("Please make the payment through your waiter.")
    elif s_c == 3:
        otp = 1904
        otp_att = int(input("\nYou have chosen DalMakhni\nEnter OTP from waiter after payment"))
        if otp_att == otp:
            print("\nSmile, your order is being prepared!")
        else:
            print("Please make the payment through your waiter.")
    
else:
    print("Enter a valid option from 1 to 4")
