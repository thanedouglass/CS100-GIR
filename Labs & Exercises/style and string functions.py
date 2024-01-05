# Q1) Write a Python function that asks for two strings as input 
# and prints True if they are equal, ignoring case, and False otherwise.
# can you do this without using an if statement? [hint: check #4 on lab 2]
user_word_1 =input("Give me a word, any word :)")
user_word_2 =input("Give me a word, any word again :0")
if user_word_1.lower() == user_word_2.lower():
    print("True")
else:
    print("False")
# Q2) Write a Python program that takes a string as input and 
#     prints two the input twice: one in all uppercase and another one in lowercase.
user_string=input("Give me a word, any word my friend")
if user_string == user_string:
    print(user_string.upper())
    print(user_string.lower())
# Q3) Write a program that asks for two inputs 
#     and prints True if their lengths are equal, and False otherwise.
first_input=len(input("What's your favorite color?"))
second_input=len(input("What's your favorite season?"))
if first_input == second_input:
    print("True")
else:
    print("False")
# Q4) Write a program that asks for two inputs
#    the first input should be a word and the second input should be an index number (int).
#    Print the letter at the given index in the given word. 
#    What happens if you give it a number that's larger than the length of the word?
# The computer will not give an output if input is larger than word length, IndexError: string index out of range
user_input_word=input("Give me a word any word my friend :)")
index_input=int(input("Give me a number any number :)"))
print(user_input_word[index_input])
# Q5) Write a Python program that takes a target substring and a source string as input 
#     and prints whether the target substring is present in the source string.
#     e.g. if target substring is "man" and the source is "human" your program should print True. 
user_substring = input("Let's play a game, give a sequence of letters, any letters: ")
user_source_string = input("Now try and give me a word using those same letters, in the same order if you dare. Or not, up to you not me :0")
if user_substring not in user_source_string:
    print(user_substring + " is not present in " + user_source_string)
else:
    print(user_substring + " is present in " + user_source_string)
# Q6) Given the string of length 4 write a program that generates a new string that 
#     prints out the reversed version of the string. E.g. if the input is "last", 
#     your program should print "tsal". Your program should prompt the user to input a four letter word.
#     You can assume the user always correctly inputs a 4 letter word.  
#     The first line is done for you. Uncomment it.
four_character_user_input=input("Give me a four letter word, any four letter word <3")
reverse_input=four_character_user_input[::-1]
print(reverse_input)
# or print(four_character_user_input[3]+four_character_user_input[2] ...)
# Q7) Given a string of length 3, write a program that prints out the number of times 
#     the letter 'a' occurs in the string. Ignore case. E.g. if the input Ana, your prgram prints 3.
len_three_input=input("Give me a three letter word any three letter word!")
green=len_three_input.count("a")
print(green)
#or
#word="Ana"
#count=0
# if word[0].lower()=="a"
    #count = count + 1
# if word[1].lower()=="a"
    #count = count + 1
# if word[2].lower()=="a"
    #count = count + 1
#print(count) 
