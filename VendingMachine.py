v = {'Chips': ["1.Kurkure Masala-Rs 40", '2.Lays West Indies Hot n Sweet-Rs 20', '3.Balaji Salted-Rs 40'],
     'Cola': ['1.Coca Cola-Rs 40', '2.Pepsi-Rs 40', '3.Thumbs Up-Rs 40'],
     'Mineral Water': ['1.Kinley-Rs 20', '2.Aquafina-Rs 20', '3.Bisleri-Rs 20'],
     'Cookies and Biscuits': ['1.Chocolate Chip Cookies-Rs 50', '2.Hide n Seek-Rs 34', '3.Dark Fantasy-Rs 54']}
c = int(input("Select your refreshment.Press\n1 - Chips\n2 - Carbonated Drinks\n3 - Mineral Water\n4 - Biscuits and Cookies:\n"))


def Chips():
    for i in v['Chips']:
        print("\n",i)
    s_c = int(input("Enter your choice in Chips:"))
    #for kurkure
    if s_c == 1:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Kurkure Masala\nEnter 40 rs into Vending Machine:"))
        qty = int(input("\nEnter how many packets you would like:"))

        total_amt = qty * 40
        change = 0
        if  total_amt > 40 and total_amt <= 1000 and ent_amt>total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 40 and total_amt <= 1000 and ent_amt<total_amt:
            change = total_amt - ent_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            Chips()
        elif total_amt < 40:
            print("Please Enter Rs 40")
            print("Please enter your choice:")
            Chips()
    #Lays
    elif s_c == 2:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Lays West Indies Hot n Sweet\nEnter 20 rs into Vending Machine:"))
        qty = int(input("\nEnter how many packets you would like:"))

        total_amt = qty * 20
        change = 0
        if  total_amt > 20 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 20 and total_amt <= 1000 and ent_amt < total_amt:
            change = total_amt - ent_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            Chips()
        elif total_amt < 20:
            print("Please Enter Rs 20")
            print("Please enter your choice:")
            Chips()
    #Balaji
    elif s_c == 3:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Balaji Salted\nEnter 40 rs into Vending Machine:"))
        qty = int(input("\nEnter how many packets you would like:"))

        total_amt = qty * 40
        change = 0
        if  total_amt > 40 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 40 and total_amt <= 1000 and ent_amt < total_amt:
            change = total_amt - ent_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            Chips()
        elif total_amt < 40:
            print("Please Enter Rs 40")
            print("Please enter your choice:")
            Chips()

def Cola():
    for i in v['Cola']:
        print("\n",i)
    s_c = int(input("Enter your choice in Cola:"))
    #Coke
    if s_c == 1:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Coca Cola\nEnter 40 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 40
        change = 0
        if  total_amt > 40 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 40 and total_amt <= 1000 and ent_amt < total_amt:
            change = total_amt - ent_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            Cola()
        elif total_amt < 40:
            print("Please Enter Rs 40")
            print("Please enter your choice:")
            Cola()
    #Pepsi
    elif s_c == 2:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Pepsi\nEnter 40 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 40
        change = 0
        if  total_amt > 40 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 40 and total_amt <= 1000 and ent_amt < total_amt:
            change = total_amt - ent_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            Cola()
        elif total_amt < 40:
            print("Please Enter Rs 40")
            print("Please enter your choice:")
            Cola()
    #Thumbs UP
    elif s_c == 3:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Thumbs UP\nEnter 40 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 40
        change = 0
        if  total_amt > 40 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 40 and total_amt <= 1000 and ent_amt < total_amt:
            change = total_amt - ent_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            Cola()
        elif total_amt < 40:
            print("Please Enter Rs 40")
            print("Please enter your choice:")
            Cola()

def MinWat():
    for i in v['Mineral Water']:
        print("\n",i)
    s_c = int(input("Enter your choice in Cola:"))
    #Kinley
    if s_c == 1:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Kinley\nEnter 20 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 20
        change = 0
        if  total_amt > 20 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 20 and total_amt <= 1000 and ent_amt < total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            MinWat()
        elif total_amt < 20:
            print("Please Enter Rs 20")
            print("Please enter your choice:")
            MinWat()
    #Aquafina
    elif s_c == 2:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Aquafina\nEnter 20 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 20
        change = 0
        if  total_amt > 20 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 20 and total_amt <= 1000 and ent_amt < total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            MinWat()
        elif total_amt < 20:
            print("Please Enter Rs 20")
            print("Please enter your choice:")
            MinWat()
    #Bisleri
    elif s_c == 3:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Bisleri\nEnter 20 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 20
        change = 0
        if  total_amt > 20 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 20 and total_amt <= 1000 and ent_amt < total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            MinWat()
        elif total_amt < 20:
            print("Please Enter Rs 20")
            print("Please enter your choice:")
            MinWat()

def CookynBis():
    for i in v['Cookies and Biscuits']:
        print("\n",i)
    s_c = int(input("Enter your choice in Cookies and Biscuits:"))
    #Choco Chip Cookies
    if s_c == 1:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Chocolate Chip Cookies\nEnter 50 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 50
        change = 0
        if  total_amt > 50 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 50 and total_amt <= 1000 and ent_amt < total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            CookynBis()
        elif total_amt < 50:
            print("Please Enter Rs 50")
            print("Please enter your choice:")
            CookynBis()
    #Hidenseek
    elif s_c == 2:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Hide n Seek\nEnter 34 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 34
        change = 0
        if  total_amt > 34 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 34 and total_amt <= 1000 and ent_amt < total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            CookynBis()
        elif total_amt < 34:
            print("Please Enter Rs 34")
            print("Please enter your choice:")
            CookynBis()
    #Dark Fantasy
    elif s_c == 3:
        print("\nPlease enter change not more than a 100rs note")
        ent_amt = int(input("You have chosen Dark Fantasy\nEnter 54 rs into Vending Machine:"))
        qty = int(input("\nEnter how many bottles you would like:"))

        total_amt = qty * 54
        change = 0
        if  total_amt > 54 and total_amt <= 1000 and ent_amt > total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 54 and total_amt <= 1000 and ent_amt < total_amt:
            change = ent_amt - total_amt
            print("Entered amount-", ent_amt, "change dropped:", change)
            print("Enjoy!")
        elif total_amt > 1000 or qty > 10:
            print("You have entered an indispensable amount. Max quantity 10 items.")
            print("Please re-enter your choice:")
            CookynBis()
        elif total_amt < 54:
            print("Please Enter Rs 54")
            print("Please enter your choice:")
            CookynBis()

        
if c == 1:
    Chips()
elif c == 2:
    Cola()
elif c == 3:
    MinWat()
elif c == 4:
    CookynBis()

#v = {'Chips': ["1.Kurkure Masala-Rs 40", '2.Lays West Indies Hot n Sweet-Rs 20', '3.Balaji Salted-Rs 40'],
#     'Cola': ['1.Coca Cola-Rs 40', '2.Pepsi-Rs 40', '3.Thumbs Up-Rs 40'],
#    'Mineral Water': ['1.Kinley-Rs 20', '2.Aquafina-Rs 20', '3.Bisleri-Rs 20'],
#     'Cookies and Biscuits': ['1.Chocolate Chip Cookies-Rs 50', '2.Hide n Seek-Rs 34', '3.Dark Fantasy-Rs 54']}
