# DO NOT MODIFY THE FUNCTION HEADER
# This is autograded. If the autograder cannot run your code, you will get a zero.
def solution(word):
    char_index = {}
    
    for i, character in enumerate(word):
        if character in char_index:
            return char_index[character]
        char_index[character] = i
        
    return -1

