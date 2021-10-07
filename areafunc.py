def area():
    L = int(input("\nEnter the length of the rectangle:"))
    W = int(input("\nEnter the width of the rectagle:"))
    b = int(input("\nEnter the base of the triangle:"))
    h = int(input("\nEnter the height of the triangle:"))
    r = float(input("\nEnter the radius of the circle:"))

    atri = 1/2*(b*h)
    arect = L*W
    acircle = 3.14*r*r
    print("The area of a rectangle with length L=",L,"and width W=",W ,"is",arect)
    print("The area of a triangle with base b=",b,"and height h=",h,"is",atri )
    print("The area of a rectangle with a radius r=",L,"is",acircle)

def swap(a,b):
    print("numbers before swapping are:a = ",a,"b=",b)
    temp = a
    a = b
    b = temp
    print("The swapped numbers are:a=",a,"and b=",b)

i = input("Enter which operation you would like to perform: a---area,s---swap")
if i == 'a':
    area()
elif i == 's':
    a = input("Enter value of 1st number:")
    b = input("Enter value of 2nd number:")
    swap(a,b)

