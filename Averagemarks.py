sub1 = int(input("marks in maths"))
sub2 = int(input("marks in science"))
sub3 = int(input("marks in hindi"))
sub4 = int(input("marks in english"))
sub5 = int(input("marks in marathi"))
total=sub1+sub2+sub3+sub4+sub5
average = total/5
print('Total marks=',total,'\nAverage is ',average)
print('Total marks='+str(total)+'\nAverage is '+str(average))
if(average>0 and average<35):
    print("failed")
elif(average>=35 and average<60):
    print("Grade B")
elif(average>=60 and average<70):
    print("G
rade A")
elif(average>=70 and average<100):
    print("Grade O")
else:
    print("Invalid"
