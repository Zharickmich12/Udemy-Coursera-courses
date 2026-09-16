#The process of identifying and removing errors from a program is called debugging
"""
Data types in Python:
    Number
        Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
        Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
        Complex: Example 1 + j, 2 + 4j
    String: A sequence of characters enclosed in single or double quotes. Example: 'Hello', "World"
    Boolean: A data type that can have one of two values: True or False
    List: An ordered collection of items enclosed in square brackets. Example: [1, 2, 3]
    Dictionary: An unordered collection of key-value pairs enclosed in curly braces. Example: {'name': 'John', 'age': 30}
    Tuple: A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.Example: (1, 2, 3)
    Set: A set is an unordered collection of unique items enclosed in curly braces. Example: {1, 2, 3}
"""
#checking the data type of a variable
x = 5
print(type(x)) # Output: <class 'int'>

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#Built-in functions
min(1, 2, 3, 4, 5) # returns the minimum value
max(1, 2, 3, 4, 5) # returns the maximum value
sum([1, 2, 3, 4, 5]) # returns the sum of all elements
dir(str) # returns all the attributes and methods of str
len('Asabeneh') # returns the length of a string
str(100) # converts an integer to a string
int('100') # converts a string to an integer
float('3.14') # converts a string to a float
input('Enter a number: ') # takes input from the user

"""
Variables
A variable refers to a memory address in which data is stored
    Python Variable Name Rules
        -A variable name must start with a letter or the underscore character
        -A variable name cannot start with a number
        -A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        -Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
snake_case: all letters are lowercase and words are separated by underscores
When we assign a certain data type to a variable, it is called variable declaration.
Assigning means storing data in the variable.
"""
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#An argument is a value which we can be passed or put inside the function parenthesis
print(len(first_name)) # 8

# Declaration of multiple variables in one line
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

"""
Checking Data types and Casting
    Check Data types: To check the data type of certain data/variable we use the type() built-in function.
"""
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

"""
Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string.
"""
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


#Exercises: Level 1
#Declare a first name variable and assign a value to it
first_name = 'Zharick'
#Declare a last name variable and assign a value to it
last_name = 'Huertas'
#Declare a full name variable and assign a value to it
full_name = 'Zharick Huertas'
#Declare a country variable and assign a value to it
Country = 'Colombia'
#Declare a city variable and assign a value to it
city = 'Bogota'
#Declare an age variable and assign a value to it
age = 21
#Declare a year variable and assign a value to it
year = 2004
#Declare a variable is_married and assign a value to it
is_married = False
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light_on = True
#Declare multiple variable on one line
first_name, last_name, full_name, Country, city, age, year, is_married, is_true, is_light_on = 'Zharick', 'Huertas', 'Zharick Huertas', 'Colombia', 'Bogota', 21, 2004, False, True, True 


#Exercises: Level 2
#Check the data type of all your variables using type() built-in function
type(first_name)
type(last_name)
type(full_name)
type(Country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
#Using the len() built-in function, find the length of your first name
len(first_name)
#Compare the length of your first name and your last name
len(first_name) == len(last_name)
#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * (30 ** 2)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * 30
#Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle: "))
area_user_circle = 3.14 * (radius ** 2)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
