n1=int(input("Enter 1st no: "))
n2=int(input("Enter 2nd no: "))
n3=int(input("Enter 3rd no: "))
if n1>n2 and n1>n3:
    print("The largest no is: ",n1)
elif n2>n1 and n2>n3:
    print("The largest no is: ",n2)
else:
    print("The largest no is: ",n3)

output:
Enter 1st no: 1000
Enter 2nd no: 8889
Enter 3rd no: 9998
The largest no is:  9998
