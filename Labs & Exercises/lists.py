#1) Create a list my_list containing 5 random integers. Print the third element of the list.
my_list=[7,8,10,4,9]
print(my_list[2])
#1.1) Append the number 6 to the end of my_list from Q1 and print out the list. 
my_list.append(6)
print(my_list)
#1.2) Replace the second element of my_list with the value 10 and print out the list to confirm. 
my_list[1]=10
print(my_list)
#1.3) Remove the first element from my_list.
my_list.pop(0)
#1.4) Check if the value 3 is in my_list. Print the result.
# if 3 in my_list:
#    print("3 is in the list")
for i in my_list:
    if i==3:
        print("3 is in the list")
        break
    else:
        print("3 is not in the list")
        break
#1.5) Find and print the index of the first occurrence of the value 4 in my_list.
for index, value in enumerate(my_list):
    if value == 4:
        print(f"The first occurrence of 4 is at index {index}")
        break
#1.6) Sort my_list in ascending order.
my_list.sort()
print(my_list)
#1.7) Reverse the order of elements in my_list.
my_list.reverse()
print(my_list)
#1.8) Create a copy of my_list called my_copy using slicing.
my_copy = my_list[:]
print(my_copy)
#1.9) Extend my_list with another list new_elements containing [7, 8, 9]. 
# Print the modified my_list.
my_list.append(7)
my_list.append(8)
my_list.append(9)
print(my_list)

