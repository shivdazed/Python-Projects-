print("Enter two numbers into the calci\n")
n1 = int(input("Enter the first number---"))

n2 = int(input("Enter the second number---"))

o = input("Choose operator--\n'+'~Addition \n'-'~Subtraction\n'*'~Multiplication\n'/'~Division\n")

if o == '+':
    print(f"The sum of {n1} and {n2} ={n1+n2}")
elif o == '-':
    print(f"The difference of {n1} and {n2} ={n1-n2}")
elif o == '*':
    print(f"The product of {n1} and {n2} ={n1*n2}")
elif o == '/':
    print(f"The quotient of {n1} and {n2} ={n1/n2}")
else:
    print("Invalid Input")
