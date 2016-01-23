#gallons = input("How many gallons you put in that car? ")
#if (gallons[0].isnumeric()==False and gallons[0] !=".") or gallons[-1].isnumeric()==False:
    #gallons = input("Enter the number of gallons in arabic numerals this time: ")
tryagain = 'start'
for tries in range(6):
    if tryagain!='yes' and tryagain!='start':
        break
    tryagain = 'start'
    if tries == 0:
        gallons = input("How many gallons you put in that car?")
    elif tries == 5:
        print("This isn't your day. Rerun the program when you're feeling up to it")
        import os
        os._exit(1)
    else:
        gallons = input("Please use only digits and decimals: $")
    gallonslist = list(gallons)
    top=len(gallonslist)
    for z in range(top):
        if gallonslist[z].isnumeric()==False and gallonslist[z]!='.':
            tryagain = 'yes'
    if gallonslist.count('.')>1:
        tryagain = 'yes'
    if tryagain != 'yes':
        tryagain = 'go'     
gallons=float(gallons)
liters = str(round(gallons * 3.7854, 3))
barrels = str(round(gallons / 19.5, 3))
price = str(round(gallons * 3.65, 2))
gallons = str(gallons)
print(gallons + " gallons of gas is equivalent to: \n" + liters + " liters of gas\n" + barrels + " barrels of oil \n" + "and $" + price)
