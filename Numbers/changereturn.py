'''
The user enters a cost and then the amount of money given. The program will
figure out the change and the number of quarters, dimes, nickels, pennies
needed for the change.
'''
total = input("Enter the total for the purchase: ")
payment = input("Enter the amount paid: ")

change = payment - total

dollars = int(change)

cointotal = (change % dollars) * 100

print "Total: {0}".format(float(total))
print "Paid: {0}".format(float(payment))

print "Change due: {0}".format(int(cointotal))
