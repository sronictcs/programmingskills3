#to loop through some numbers use the range function
#with the parameters(start, stop, step)
for value in range (1, 5):
    print(value)
    
#you can using range to populate a list
numbers = list(range(1, 6))
print(numbers)

#remember start, stop, step?
even_numbers = list(range(2, 11, 2))
print(even_numbers)


#You can appending values to a new list from calculated range
squares = []
for value in range (1, 11):
    square = value**2
    squares.append(square)
print (squares)

#using other functions on lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


'''4-3. Counting to Twenty: Use a for loop to print the numbers
from 1 to 20, inclusive.'''
print("4-3")

'''4-4. One Million: Make a list of the
numbers from one to one million, and then use a for loop to print
the numbers. (If the output is taking too long, stop it by pressing
ctrl-C or by closing the output window.)'''
print("4-4")

'''4-5. Summing a Million: Make a list of the numbers from one to one
million, and then use min() and max() to make sure your list actually
starts at one and ends at one million. Also, use the sum() function
to see how quickly Python can add a million numbers.'''
print("4-5")
 
'''4-6. Odd Numbers: Use the third argument of the range() function to
make a list of the odd numbers from 1 to 20. Use a for loop to print
each number.'''
print("4-6")

'''4-7. Threes: Make a list of the multiples of 3 from 3 to 30.
Use a for loop to print the numbers in your list.'''
print("4-7")

'''4-8. Cubes: A number raised to the third power is called a cube.
For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each
integer from 1 through 10), and use a for loop to print out
the value of each cube.'''
print("4-8")


