try:
    age= int(input("Enter your age:"))
    if age < 18:
        raise Exception("You are not old enough. Sorry!")
except Exception as e:
    print(e)

finally:
    if age >= 18:
        print("You are old enough")
    
