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