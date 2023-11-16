fruits=["apples","bananas","cherry"]
fruits[1]="mangoes"
print(fruits)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.append("blackberry")
print(thislist)

thislist.insert(2,"doggy")
print(thislist)

onemorelist=["doogy","coogy","soogy"]
thislist.extend(onemorelist)
print(thislist)


#remove items in a list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.remove("apple")
print(thislist)  #remove() method removes sepcified item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.pop(2) #pop() remove item at given index if index is mentioned
print(thislist) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
del thislist[0]
print(thislist)

list=[40,20,30,10]
newlist=[]
for i in list:
    if i>25:
        newlist.append(i)
print(newlist)

list=[10,20,[30,40,50],60,70]
print(list[2])
print(list[2][1])



n=int(input("Enter no of elements: "))
list= []
for i in range(n):
    num=int(input())
    list.append(num)
idx1=int(input("Enter index1: "))
idx2=int(input("Enter index2: "))
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp
print(list)


output:
['apples', 'mangoes', 'cherry']
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango', 'blackberry']
['apple', 'blackcurrant', 'doggy', 'watermelon', 'orange', 'kiwi', 'mango', 'blackberry']
['apple', 'blackcurrant', 'doggy', 'watermelon', 'orange', 'kiwi', 'mango', 'blackberry', 'doogy', 'coogy', 'soogy']
['banana', 'cherry', 'orange', 'kiwi', 'mango']
['apple', 'banana', 'orange', 'kiwi', 'mango']
['apple', 'banana', 'cherry', 'orange', 'kiwi']
['banana', 'cherry', 'orange', 'kiwi', 'mango']
[40, 30]
[30, 40, 50]
40
Enter no of elements: 4
23
65
19
90
Enter index1: 0
Enter index2: 2
[19, 65, 23, 90]
> 
