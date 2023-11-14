num1=int(input("Enter no 1: "))
num2=int(input("Enter no 2: "))
operator=input("Enter operator: ")
match operator:
    case "+":
        print("Sum is",num1+num2)
    case "-":
        print("Difference is",num1-num2)
    case "*":
        print("Product is:",num1*num2)
    case "/":
        print("Quotient is: ",num1/num2)
    case "_":
        print("Enter a valid no")

output:
1) Enter no 1: 12
Enter no 2: 14
Enter operator: +
Sum is 26
2)Enter no 1: 12
Enter no 2: 14
Enter operator: -
Difference is -2
3)Enter no 1: 12
Enter no 2: 14
Enter operator: *
Product is: 168
4)Enter no 1: 50
Enter no 2: 25
Enter operator: /
Quotient is:  2.0
