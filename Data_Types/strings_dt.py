name = 'python'
greeting = "Hello"
multiline = '''This 
is a 
multiline string'''

string1 = "Python Programming"

# Accessing individual characters and slices
print(string1[0])             # Prints first character: 'P'
print(string1[0:4])           # Prints first 4 characters: 'Pyth'
print(string1[-1])            # Prints last character: 'g'
print(string1[0:4:2])         # Prints first 4 characters with step 2: 'Pt'

# String case conversion
print(string1.lower())        # Converts to lowercase: 'python programming'
print(string1.upper())        # Converts to uppercase: 'PYTHON PROGRAMMING'

# String length
print(len(string1))           # Returns the length: 18

# Trimming whitespace and replacing text
string2 = '   ABC String   '
print(string2.strip())        # Removes leading/trailing whitespace: 'ABC String'
print(string2.replace('ABC', 'PQR'))  # Replaces 'ABC' with 'PQR': '   PQR String   '

# Splitting and finding substrings
string3 = 'HTML, CSS, JS, Python'
print(string3.split(', '))    # Splits into list: ['HTML', 'CSS', 'JS', 'Python']
print(string3.find('CSS'))    # Finds index of 'CSS': 6

# Counting substrings
string4 = 'Web Web Web Development'
print(string4.count('Web'))   # Counts 'Web': 3

# String formatting
product = 'Laptops'
quantity = 5
order = "We have ordered {} {}"
print(order.format(quantity, product))  # Output: 'We have ordered 5 Laptops'

# Escaped quotes
message = "Python is a \"programming language\""
print(message)                # Output: Python is a "programming language"

# Raw string (e.g., file paths)
path = r"C:\Users\User\Documents\file.txt"
print(path)                   # Output: C:\Users\User\Documents\file.txt

# Membership check
print("Python" in message)    # Checks if 'Python' is in the message: True

# F-string example
language = "Python"
feature = "popular"
print(f"{language} is a {feature} language.")  # Output: Python is popular language.
