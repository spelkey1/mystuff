tryagain = 'start'
for tries in range(6):
    if tryagain!='yes' and tryagain!='start':
        break
    tryagain = 'start'
    if tries == 0:
        price = input("Enter the price of a meal: $")
    elif tries == 5:
        print("This isn't your day. Rerun the program when you're feeling up to it")
        import os
        os._exit(1)
    else:
        price = input("Please use only digits and decimals: $")
    pricelist = list(price)
    top=len(pricelist)
    for z in range(top):
        if pricelist[z].isnumeric()==False and pricelist[z]!='.':
            tryagain = 'yes'
    if pricelist.count('.')>1:
        tryagain = 'yes'
    if tryagain != 'yes':
        tryagain = 'go'
price=float(price)
price=round(price, 2)
tip = round(price * 0.16, 2)
total = round(price + tip, 2)
tip = str(tip)
total = str(total)
print("A 16% tip would be $" + tip +",")
print("Which makes the total price of your meal: $" + total)
total=float(total)
if total > 150:
    print("Big Spender.")

