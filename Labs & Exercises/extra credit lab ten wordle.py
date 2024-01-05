import random
import sys

def main():

    guess_count = 0 # Initialize the counter

    # Ask the user for the game mode
    mode = input("Choose the game mode (Normal/Hard): ").lower()

    if mode == "hard":
        max_guesses = 6  # Set the maximum number of guesses for Hard Mode
    else:
        max_guesses = 7  # Set the maximum number of guesses for Normal Mode

    # Check if the length of the guess is 5
    while guess_count<max_guesses:
        answer = getRandomWord().lower()
        guess = input("Enter a 5 letter guess?\n").lower()  # Ask for input and convert to lowercase

        # Input validation: Check if the length of the guess is 5
        while len(guess) != 5:
            print("Please enter a 5 letter word.")
            guess = input("Enter a 5 letter guess?\n").lower()


        for i in range(len(guess)):  # Iterate over the five characters in the user guess (index)
            if guess[i] == answer[i]:
                print(guess[i] + " - Green" )  # Mark correct letter and position as green
            elif guess[i] in answer:
                print(guess[i] + " - Yellow")  # Mark correct letter in incorrect position as yellow
            else:
                print(guess[i] + " - Red")  # Mark incorrect letter as red

        guess_count += 1
        if guess == answer:
            print("You Won! That took", guess_count, "guess(es).")
            break

    if guess_count == max_guesses and guess != answer:
        print("You lost. The answer was " + answer + ".")

# A helper method that prints the guess with the
# correct colors to the console.
# TODO: complete this function.
#def printGuessColors(guess, answer):

    # Ask the user for input and as long as there's an attempt left, 
    # give the user feedback by printing a message as described in the instructions.
     

# A helper method that prints the guess with the
# correct colors to the console.
# A helper method that determines the color
# of the letter in the guess.
# TODO: complete this function to return "Yellow", "Red", or "Green".
#def letterColor(index, guess, answer):

# A method that gets a random word from a file.
# DO NOT MODIFY THIS.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]
        file.close()
        return random.choice(words)


main()
