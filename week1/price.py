price = input("Enter the price of a meal: $")
if price[0].isnumeric()==False:
    price = input("Enter the price of a meal in arabic numerals this time: $")
price=float(price)
tip = round(price * 0.16, 2)
total = price + tip
tip = str(tip)
total = str(total)
print("A 16% tip would be $" + tip +",")
print("Which makes the total price of your meal: $" + total)
total=float(total)
if total > 150:
    print("Big Spender.")

 
