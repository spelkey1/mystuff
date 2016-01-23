print("Let's find some averages")
#prompts for a number and validates it
tryagain = 'start'
for tries in range(6):
    if tryagain!='yes' and tryagain!='start':
        break
    tryagain = 'start'
    if tries == 0:
        number1 = input("Enter a number ")
    elif tries == 5:
        print("This isn't your day. Rerun the program when you're feeling up to it")
        import os
        os._exit(1)
    else:
        number1 = input("Please use only digits, decimals, and negative signs: ")
    number1list = list(number1)
    top=len(number1list)
    for z in range(top):
        if number1list[z].isnumeric()==False and number1list[z]!='.' and number1list[z]!='-':
            tryagain = 'yes'
    if number1list.count('.')>1 or number1list.count('-')>1:
        tryagain = 'yes'
    if (number1list[0]!='-' and number1list.count('-')==1):
        tryagain = 'yes'
    if tryagain != 'yes':
        tryagain = 'go'
#prompts for a second number and validates it
tryagain = 'start'
for tries in range(6):
    if tryagain!='yes' and tryagain!='start':
        break
    tryagain = 'start'
    if tries == 0:
        number2 = input("Enter a second number ")
    elif tries == 5:
        print("This isn't your day. Rerun the program when you're feeling up to it")
        import os
        os._exit(1)
    else:
        number2 = input("Please use only digits, decimals, and negative signs: ")
    number2list = list(number2)
    top=len(number2list)
    for z in range(top):
        if number2list[z].isnumeric()==False and number2list[z]!='.'and number2list[z]!='-':
            tryagain = 'yes'
    if number2list.count('.')>1 or number2list.count('-')>1:
        tryagain = 'yes'
    if (number2list[0]!='-' and number2list.count('-')==1):
        tryagain = 'yes'
    if tryagain != 'yes':
        tryagain = 'go'
number1 = float(number1)
number2 = float(number2)
arimean = str((number1 + number2)/2)
geomean = str((number1 * number2)**.5)
rootmean =str((number1**2 + number2**2)**.5)
print("The arithmetic mean is: " + arimean)
print("The geometric mean is: " + geomean)
print("The root-mean-square is: " + rootmean)

