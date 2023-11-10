# string
name= "Manish"

# integer
roll_number= 17

# floating no
percentage= 95.8

#boolean
is_student= True

print(name)
print(type(name))
print(roll_number)
print(type(roll_number))
x = 5
y = 10
print(x + y)
# output multiple variables
print(name, roll_number, percentage, is_student, x, y, x+y)

percentage= 94
print(name, roll_number, percentage, is_student, x, y, x+y)

print("My name is " + name)

# print(x + y + name)

# print("My name is " + name " and my roll no is " + roll_number)

#print expressions
print("My percentage has changed to",percentage - 1.0)

#print with separator
print(name, roll_number, percentage, is_student, x, y, x+y, sep="-")

x=1
y=2
z=3
print(x,y,z,sep="->")
