# Q1) create an empty dictionary and add the following key-value pair to it:
# key "Howard" value "Bison"
user_dict={}
user_dict["Howard"]="Bison"
# 1.1) print the value of the key Howard from the previous dictionary 
print(user_dict["Howard"])

# 1.2) modify the value associted with Howard and change it to "university"
user_dict["Howard"]="university"
# Q2) Write a function that takes a dictionary and a key as inputs and returns a boolean
def key_exists(my_dict, key):
    return key in my_dict
user_dictionary={"Howard":"Bison", "George":"Town", "John":"Hopkins"}
result_boolean = key_exists(user_dict, "Howard")
print(result_boolean)
# indicating if the key exists in the dictionary 

# Q3) Write a function that takes a dictionary and a value as inputs and returns a boolean indicating 
# if the value is associated with any key in the dictionary 
def value_key (my_input, value):
    return value in my_input
new_dictionary={"Name": "Thane", "Age": "Eighteen", "Height": "Six Foot"}
value_boolean = value_key(new_dictionary, "Thane")
print(value_boolean)
# Q4) Write a function that takes a list of strings (all unique) as input, 
# and returns a dictionary that maps each word to its length.
# e.g. for input list ['apple', 'banana', 'date']
# return the dictionary {'apple' : 5, 'banana' :6, 'date': 4}
def problem_four(user_list):
    length_dict = {}
    for word in user_list:
        length_dict[word] = len(word)
    return length_dict

string_list = ["apple", 'banana', 'date']
result_dict = problem_four(string_list)
print(result_dict)

# Q5) Write a function that takes a dictionary and an age threshold int as input. The dictionary 
# contains student names (key) and their ages (value). Return a new dictionary that contains 
# student name : age mapping of only those students who are strictly older than the threshold age. 
# e.g. if the threshold age is 12, the new dictionary should only have students 13 years and above. 
def problem_five(dictionary, age_threshold):
    one_dict = {}
    for student, age in dictionary.items():
        if age >= age_threshold:
            one_dict[student] = age
            return one_dict
profile_dict = {"Thane": 18, "Alana": 19, "Christian": 20, "Jesus": 4}
age_threshold = 12
result_dict = problem_five(profile_dict, age_threshold)
print(result_dict)


