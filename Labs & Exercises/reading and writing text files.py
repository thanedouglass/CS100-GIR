#Feel free to look at these code snippets as you complete your exercise questions 

# example 1: opening a file 
in_file = open("states.txt", "r")
for line in in_file:
    print(line.strip()) # what does strip do? 
    in_file.close()
# example 2: writing to a file
out_file = open("gettysburg.txt", "w")
out_file.write("Four score and seven years ago our fathers brought forth on this continent, a new nation.\n")
out_file.close()


#Q1) Open the states.txt file and print out all the states that start with letters N and M. 
in_file_one = open("state.txt", "r")
    for line in in_file_one:
        if line.strip().startswith("N") or line.strip().startswith("M"):
            return(line.strip())
            in_file_one.close()
#index = in_file_one.index("N")
#count = 0
#while True:
#    count += 1
#for line in in_file_one:
    
#Q2) Write a program to determine the state with the longest name.

in_file_two = open("state.txt", "r")
longest_state = ""
longest_length = 0
    for line in in_file_two:
        state_name = line.strip()
        state_length = len(state_name)
        if state_length > longest_length:
            state_name = longest_state
        return ("State with the longest name:", longest_state)
        in_file_two.close()
#Q3) Write code to determine if the answer to #2 unique. Collect all the states with the longest name 
# in a list, and print the list 
longest_states_list = []
in_file_three = open("states.txt", "r")
the_longest_length = len(longest_length)
    for line in in_file_three:
        state_name = line.strip()
        if line==len(longest_state):
            longest_states_list.append(state_name)
        return longest_states_list
        in_file_three.close()
#Q4) Write a program that opens the file numbers.txt and writes all even numbers from 2 to 10,000 [each number in a separate line]
out_file = open("numbers.txt", "w")
    for number in range(2,10001):
        if number%2==0:
            out_file.write(str(number) + "\n")
        out_file.close()
