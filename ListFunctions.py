a = []

n = int(input("Enter the number of elements in the List:"))

for i in range(n):
    l = input("Enter an element")
    a.append(l)

print("\nList is:",a)


def ListOps():
    o = input("\nEnter the operation you would like to perform on list:\n1.Append\n2.Extend\n3.Count\n4.Index\n5.Clear\n6.Remove\n7.Copy\n8.Length\n9.Insert\n10.Pop\n11.Exit\n\n\n\n")
    while(o != '11'):
        if o == '1':
            ap_e=input("\nEnter element you wish to append to list:\n")
            a.append(ap_e)
            print("\nAppended List is:\n",a)
            
        elif o == '2':
            x = int(input("\nEnter the number of elements you wish to add or extend inital list by:\n"))
            for i in range(x):
                j = input("\nEnter an element")
                a.extend(j)
            print("\nExtended list is:",a)
            
        elif o == '3':
            c_el= input("\nEnter an element you wish to find the count for:")
            a.count(c_el)
            print("\nThe Count or number of data elements in the list is:",a)
        elif o == '4':
            dat_el=input("\nEnter the element you wish to find the index of:")
            a.index(dat_el)
            print("\nThe position or index of the data element is:",a)
        elif o == '5':
            a.clear()
            print("\nThe list value after clearing is:",a)
        elif o == '6':
            re_el=input("\nEnter the element to be removed:")
            a.remove(re_el)
            print("\nThe new list after removing element is:",a)
        elif o == '7':
            new_l = a.copy()
            print("\nThe copy of the list is:",new_l)
        elif o == '8':
            print("\nThe length of the list is:",length(a))        
        elif o == '9':
            p = int(input("\nEnter the index position you want to add an element:\n"))
            e= input("\nEnter the element you wish to add:")
            a.insert(p,e)
            print("The new list is:",a)
        elif o == '10':
            p = int(input("Enter the index of the element you wish to pop(last element in list is popped)):"))
            pop_e = a.pop(p)
            print("\nThe popped elements is:",pop_e)
            print("\nThe new list is :",a)
        break

ListOps()
choice = input("Do you wish to continue enter Y for Yes and N for No:")
while choice == 'Y':
    ListOps(o)
    if choice == 'N':
        break
