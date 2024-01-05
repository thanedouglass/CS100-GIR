def collect_column_items(matrix, n):        
    column_to_return = n
    return_lst = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column == column_to_return:
                return_lst.append(matrix[row][column])
    return return_lst


def get_char_counts(word):
    dictionary = {}
    for char in word:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary

# Brownies 
remaining_brownies = 50
while remaining_brownies > 0:
    requested_brownies = int(input("How many brownies would you like? "))
    if requested_brownies < 1:
        print("Please enter a positive number")
    elif requested_brownies > remaining_brownies:
        print("Sorry I only have {} brownies left".format(remaining_brownies))
    else:
        print("OK! Here's {} brownies".format(requested_brownies))
        remaining_brownies = remaining_brownies - requested_brownies
print("We've sold all the brownies!")

# Capitalize vowels 
def capitalize_vowels(word):
    result = ""
    for char in word:
        if char in "aeiou":
            char = char.upper()
        result += char
    return result
