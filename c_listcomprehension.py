#iterating through a string using a for loop
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

#iterating through a list using List Comprehension
h_letters = [ letter for letter in 'human' ]
print( h_letters)

#a list comprehension allows you to generate a list on 1 line
#it works using an [expression for item in list]
#they are are really good because they identify when they
#recieve a string or a tuple(coming up soon!) and work on
#it like a list

#you can use a list comprehension for generating square numbers up to 100
squares = [value**2 for value in range(1,11)]
print (squares)    
'''4-9. Cube Comprehension: Use a list comprehension to generate
a list of the first 10 cubes.'''



