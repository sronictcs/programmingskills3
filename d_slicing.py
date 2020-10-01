#slicing a list means returning only part of a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

#You can loop through a slice of a list
print("Here are the players on the team:")
for player in players[:3]:
    print(f"{player.title()}")

my_foods = ["pizza", "falafel","carrot cake"]
#creating a copy of a list using no start or end slice with [:] makes a new list
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My fave foods are: {my_foods}")
print(f"My friend's foods are: {friend_foods}")
#can you see the difference in the 2 lists, they are now seperate but started the same

'''4-10. Slices: Using one of the programs you wrote
in this session, add several lines to the end of the
program that do the following:
•	Print the message The first three items
in the list are:
. Then use a slice to print the first three items
from that program’s list.
•	Print the message Three items from the middle
of the list are:
. Use a slice to print three items
from the middle of the list.
•	Print the message The last three items in the
list are:
. Use a slice to print the last three items in the list.'''

print("4-10")


'''4-11. My Pizzas, Your Pizzas: Start with your program
from Exercise 4-1 (page 56). Make a copy of the list of pizzas,
and call it friend_pizzas. Then, do the following:
•	Add a new pizza to the original list.
•	Add a different pizza to the list friend_pizzas.
•	Prove that you have two separate lists.
Print the message My favorite pizzas are:, and then use a
for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop
to print the second list. Make sure each new pizza is stored
in the appropriate list.'''
print("4-11")

    

'''4-12. More Loops: All versions of foods.py in this section
have avoided using for loops when printing to save space.
Choose a version of foods.py, and write two for loops to print
each list of foods.'''
print("4-12")

