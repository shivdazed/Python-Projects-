try:
    a = int(input("Enter the number A:"))
    b = int(input("Enter the number B:"))
    c = a/b
    print(c)
#except Exception as e:
#   print(e)

except ZeroDivisionError:
    print("We can't divide by zero")
except ValueError:
    print("Your entered value is wrong")

finally:
    print("Sum = ",a+b)
