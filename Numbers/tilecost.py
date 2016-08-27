width = input("Input width of floor (in feet): ")
length = input("Input length of floor (in feet): ")
cost = input("Input cost of tile (per square foot)")

print "The cost to cover " + str(width * length) + \
      " square feet is $" + str(width * length * cost)
