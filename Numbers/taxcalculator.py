# Asks the user to enter a cost and either a country or state tax.
# It then returns the tax plus the total cost with tax.
# Needs to round the digits down to two decimal places
# Needs to have currency formatting

total = float(raw_input("Enter the subtotal of the purchase: "))
taxInput = raw_input("Enter the tax rate or press Enter for the default rate:")
if taxInput == "":
    taxRate = 0.08
else:
    taxRate = float(taxInput)

print 'Subtotal: ', total
print "Tax: ", total * taxRate
print "Total: ", total * (1 + taxRate)
