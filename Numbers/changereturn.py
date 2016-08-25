total = input("Enter the total for the purchase: ")
payment = input("Enter the amount paid: ")

change = payment - total

dollars = int(change)

cointotal = (change % dollars) * 100

print int(cointotal)
