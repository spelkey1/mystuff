price = input("Enter the price of a meal: $")
#if (price[0].isnumeric()==False and price[0] != ".") or price[-1].isnumeric()==False:
    #price = input("Enter the price of a meal in arabic numerals this time: $")
if price.isnumeric()==False and price.count('.')!=1:
    price = input("Enter the price of a meal in arabic numerals this time: $")
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
