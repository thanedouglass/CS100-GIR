# Question 1: Create a set named 'fruits' with the following elements: 'apple', 'banana', 'orange'.
fruits = {'apple','banana','orange'}
# Question 2: Add 'strawberry' to the 'fruits' set.
fruits.add('strawberry')
# Question 3: Create a tuple named 'coordinates' with latitude and longitude values (40.7128, -74.0060).
coordinates=(40.7128,-75.0060)
# Question 4: Convert the 'fruits' set into a list.
convert_list = []
for fruit in fruits:
    convert_list.append(fruit)
# Question 5: Create a set 'colors' with the elements: 'red', 'blue', 'green', 'blue'.
colors = {'red','blue','green', 'blue'}

# Question 6: Find the number of unique colors in the 'colors' set.
for color in colors:
    print("The unique colors in the set are as follows  " + color)

# Question 7: Remove 'banana' from the 'fruits' set.
fruits.remove('banana')

# Question 8: Check if 'apple' is in the 'fruits' set and print the result.
if 'apple' in fruits:
    print("Apple is in the fruits set.")
# Question 9: Create a new set 'berries' with elements: 'strawberry', 'blueberry', 'raspberry'.

berries = {'strawberry', 'blueberry', 'raspberry'}

# Question 10: Find the common elements between the 'fruits' and 'berries' sets.
ajoined=fruits.intersection(berries)
print(ajoined)
