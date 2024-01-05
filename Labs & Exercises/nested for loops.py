import requests
response = requests.post(
    'https://pixcut.wondershare.com/openapi/api/v1/matting/removebg',
    files={'content': open('/path/to/file.jpg', 'rb')},
    headers={'appKey': 'INSERT_YOUR_API_KEY_HERE'},
)
with open('out.png', 'wb') as out:
    out.write(response.content)#
# Complete the following functions. 
# Please do not rename or modify the function names or parameters as this may cause the grader to crash. 
# For all the questions given below, your program needs to read the the us_city_population.txt file.

# HINTS:
# the split function is your friend! https://www.programiz.com/python-programming/methods/string/split
# The readlines() function might be helpful to you. Check the code example in method 1: https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/  

# Q1) Write a function that reads the us_city_population.txt file, 
# and returns a list of cities that have 1 million or more residents. 
# To receive full credit, the list needs to be sorted alphabetically.
def big_cities():
    citites = []
    infile=open('us_city_population.txt','r')
        for line in infile:
           parts = line.strip().split(',') # splits the lines at comma
            if len(parts) == 2: #seperate data parts into two parts 
                city, population = parts #initilizes parts as city and populatoin
                population = int(population) #converts population string to integer
                if population >= 1000000: #filters low populationa
                    cities.append(city) #adds all cities that fit criteria in list
    cities.sort()
    return cities
    infile.close()
# Q2) Write a function that reads the us_city_population.txt file and
# returns a dictionary indicating how many cities we have from each state.
# For instance, if we have 10 cities from CA, one entry in the dictionary should be "CA" : 10 
# Hint: checkout the split function in python
def state_city_count():
     state_dict = {
        'AL': {},
        'AK': {},
        'AZ': {},
        'AR': {},
        'CA': {},
        'CO': {},
        'CT': {},
        'DE': {},
        'FL': {},
        'GA': {},
        'HI': {},
        'ID': {},
        'IL': {},
        'IN': {},
        'IA': {},
        'KS': {},
        'KY': {},
        'LA': {},
        'ME': {},
        'MD': {},
        'MA': {},
        'MI': {},
        'MN': {},
        'MS': {},
        'MO': {},
        'MT': {},
        'NE': {},
        'NV': {},
        'NH': {},
        'NJ': {},
        'NM': {},
        'NY': {},
        'NC': {},
        'ND': {},
        'OH': {},
        'OK': {},
        'OR': {},
        'PA': {},
        'RI': {},
        'SC': {},
        'SD': {},
        'TN': {},
        'TX': {},
        'UT': {},
        'VT': {},
        'VA': {},
        'WA': {},
        'WV': {},
        'WI': {},
        'WY': {}
    }
    infiletwo=open("us_city_population", "r")
        for line in infiletwo:
            parts = line.strip().split(',')
            if len(parts) == 2:
                state, city = parts
                if state in state_dict:
                    if city not in state_dict[state]:
                        state_dict[state][city] = 1
                    else:
                        state_dict[state][city] += 1
    return state_dict
# Q3) Some cities in different states have the same names. 
# For instance, Selma is a city in both CA and AL, while Sun City is both in AZ and CA. 
# Write a function that returns a list of popular city names 
# (defined as names that appear at least 7 times in the file). 
# Washington is one such name, appearing 7 times in the file.
# The list should include each city only once. 
# To receive full credit, the list must be sorted alphabetically and the list must contain only city names (no state or population information)
def popular_names():
    city_counts = {}
    popular_city_list = []
    with open("us_city_population", "r") as infile:
        for line in infile:
            parts = line.strip().split(",")
            if len(parts) == 2:
                city, population = parts[0], int(parts[1])
                if city in city_counts:
                    city_counts[city] += 1
                else:
                    city_counts[city] = 1

    for city, count in city_counts.items():
        if count >= 7:
            popular_city_list.append(city)

    popular_city_list.sort()
    return popular_city_list

# Q4) Write a function that takes line number as input and returns the name of the city on that line.
# For instance, if the input is 2, your function should return the string "Albertville" (not the whole line!)
# If the input is an invalid number (negative number, zero, too large), return an empty string. 
def city_on_line(line_number):
    city_name = ""
    
    # Check if the input line number is valid
    if line_number <= 0 or line_number > 4:
        return city_name
    
    with open("us_city_population", "r") as infile:
        for i, line in enumerate(infile, start=1):
            if i == line_number:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    city_name = parts[0]
                break

    return city_name

line_number = int(input("Enter a line number: "))

result = city_on_line(line_number)

if result:
    return(f"The city name on line {line_number} is: {result}")
else:
    return("Invalid line number.")


