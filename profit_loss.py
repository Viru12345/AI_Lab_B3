cp= int(input("Enter cost price: "))
sp= int(input("Enter selling price: "))
if sp>cp:
    print("U hv made a profit!")
    profit= sp - cp;
    print("Profit made = ",profit)
elif cp>sp:
    print("U have incurred loss")
    loss= cp - sp;
    print("Loss incurred= ",loss)
elif cp==sp:
    print("no loss, no profit")
