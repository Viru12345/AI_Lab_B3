a = "Hello, World!"
print(a[1])
print(len(a))
print(a[5])
print(a[6])

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
print("freeg" in txt)

print(a[2:5])
print(a[2:])
print(a[:5])

print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!" removes whitespace from beg or end 
print(a.replace("H", "J")) #replaces a string(H) with another string(J)
print(a.split(",")) # returns ['Hello', ' World!']

#string concatenation
a = "Hello" #merge a with b into var c using + op
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"  #To add a space between them, add a " ":
c = a + " " + b
print(c)
