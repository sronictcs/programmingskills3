#a tuple is an immutable data type, as it once created it cannot be changed
#useful for CONSTANTS

#defining a tuple
dimensions = (200, 50)


#defining a tuple with only one element, needs trailing comma,
my_t = (3.147,)

#writing over a tuple
print ("original dimensions:")
for dimension in dimensions:
    print(dimension)
#you have to replace the values in a tuple with another set of values
dimensions = (400, 600)
print("modified dimensions:")
for dimension in dimensions:
    print(dimension)

'''4-13. Buffet: A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple.
•	Use a for loop to print each food the restaurant offers.
•	Try to modify one of the items, and make sure that Python rejects the change.
•	The restaurant changes its menu, replacing two of the items with different foods.
Add a line that rewrites the tuple, and then use a for loop
to print each of the items on the revised menu. '''
print("4-13")
