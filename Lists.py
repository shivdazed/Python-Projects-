a = []

n = int(input("Enter the number of elements in a list:"))

for i in range(n):
    r=int(input("Enter an element:"))
    a.append(r)

print("List of elements is:",a)

b = list(filter(lambda x:x>0,a))

c = list(filter(lambda x:x<0,a))

d = list(map(lambda x:x**2,a))

e = list(map(lambda x:x**3,a))

print("List of positive elements are:",b)
print("List of negative elements are:",c)
print("List of squared elements are:",d)
print("List of cubed elements are:",e)

