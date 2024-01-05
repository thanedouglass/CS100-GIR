# Please name your functions and variables appropriately. We'll take style into account while grading.

# 1) Write a function that takes two integers (num1 and num2) as input and prints their sum.
def summation(num_one,num_two):
    print(int(num_one)+int(num_two))
summation("1","5")
summation("10","30")
summation(4,80)
summation(100,9600)

# 2) Write a function that takes an integer as input and prints "Even" if it's even and "Odd" if it's odd.
def classi_num(interger):
    interger=int(interger)
    if interger%2==0:
        print("Is Even")
    else:
        print("Is Odd")
classi_num(100)
classi_num(33)
# 3) Write a function that takes a string as input and prints the count of vowels (a, e, i, o, u) in it.
#def vowels_frequency(userstring):
#    vowel_count=0
#    for j in userstring:
#        if char.lower(userstring) in 'aeiou':
#             vowel_count += 1
#    return vowel_count
#userstring = input("Give me a word: ")
#count = vowels_frequency(userstring)
#print(f"Number of vowels in '{userstring}': {count}")
# 4) Define a function that checks if a given string is a palindrome (reads the same forwards and backward)
def is_palindrome(input_string):
    clean_string = ''.join(input_string.split()).lower()
            print("True")
        else:
            print("False")
#    and prints True if the given string is a palindrome and False otherwise. Your program should be case insensitive. 
#    for a given string an easy way to get its reversed form is using this shortcut the_string[::-1]

# 5) Write a Python program that generates a random number between 1 and 100 and asks the user to guess it. 
#    Provide feedback on whether the guess is too high or too low until the user guesses correctly. 
#    To generate a random number type 'import random' without the quotes before you define your function 
#    and initialize your number like so inside your function: 
#    random_num = random.randint(a,b) where a and b are integers. This will generate a random number between a and b, including a and b. 
import random

def guess_the_number():
    random_num = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            elif user_guess < random_num:
                print("Too low! Try again.")
            elif user_guess > random_num:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_num} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

# 6) Create a function that takes a string as input and prints the count of words in the string. 
#    Words are separated by spaces. Assume the input does not have multiple spaces.
#    E.g. if the input is "a simple example" your program should print 3.
#    if the input is "Hello, world" your program should print 2. 
#    hint: as you loop, keep track of whether you're inside a word or not 
def count_words(input_string):
    # Initialize a variable to keep track of the word count
    word_count = 0
    
    # Initialize a flag to check if you're inside a word
    inside_word = False
    
    # Iterate through each character in the input string
    for char in input_string:
        # If the character is a space and you were previously inside a word, increment the word count
        if char == ' ' and inside_word:
            word_count += 1
            inside_word = False
        # If the character is not a space, set inside_word to True to indicate you're inside a word
        elif char != ' ':
            inside_word = True
    
    # After the loop, if you were inside a word, increment the word count one last time
    if inside_word:
        word_count += 1
    
    # Print the final word count
    print(word_count)

# Test cases
count_words("a simple example")  # Output should be 3
count_words("Hello, world")      # Output should be 2


# 7) Define a function that takes a sentence as input and prints the same sentence with the first letter of each word capitalized.
#    e.g. for the input "An example sentence" your program should print "An Example Sentence"
def capitalize_first_letter(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize an empty list to store the capitalized words
    capitalized_words = []
    
    # Iterate through each word and capitalize the first letter
    for word in words:
        capitalized_word = word[0].upper() + word[1:]
        capitalized_words.append(capitalized_word)
    
    # Join the capitalized words back into a sentence
    capitalized_sentence = ' '.join(capitalized_words)
    
    # Print the capitalized sentence
    print(capitalized_sentence)

# Test case
capitalize_first_letter("An example sentence")  # Output should be "An Example Sentence"



# 8) Write a function that takes a sentence (a string with words separated by spaces) as input 
#    and prints the longest word in the sentence.
def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize variables to keep track of the longest word and its length
    longest_word = ""
    max_length = 0
    
    # Iterate through each word and update the longest_word and max_length if needed
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            longest_word = word
            max_length = word_length
    
    # Print the longest word
    print("The longest word in the sentence is:", longest_word)

# Test case
find_longest_word("This is a test sentence to find the longest word")  # Output should be "The longest word in the sentence is: sentence"

# Extra credit 

# 9) Implement a function that takes a string and a substring as input and prints the 
#    count of occurrences of the substring within the string.
# e.g. if the string is "hello" and the substring is "l" your program should print 2 
# for string: "programming is fun and programming is challenging" substring: "programming" program should print 2. 






