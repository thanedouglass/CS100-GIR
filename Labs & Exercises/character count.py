# DO NOT MODIFY LINE 1 as this may crash the autograder.
def get_char_counts(word):

    dictionary = {}
    for char in word:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary


# DO NOT MODIFY THIS PART.
if __name__ == '__main__':
    n = input('Enter a word: ')
    print(get_char_counts(n))
