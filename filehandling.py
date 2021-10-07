file = open(r'C:\Users\anuro\Desktop\student.txt','r')

n = input("Enter your name:")
std = int(input("\Enter which standard you are in currently:"))
std_id = input("\Enter your student ID:")

m = []
print("Enter the marks of Five Subjects,Physics Chemistry Maths Biology English:")
for i in range(5):
    r =int(input("Enter the marks:))
    m.append(r)
