# Python Programming Workshop Documentation

## For BTEC Level 1, Level 2, and Level 3 Students

---

## Table of Contents

1. [Introduction to Python](#introduction-to-python)
2. [Setting Up Python](#setting-up-python)
3. [Level 1 - Foundation](#level-1---foundation)
4. [Level 2 - Intermediate](#level-2---intermediate)
5. [Level 3 - Advanced](#level-3---advanced)
6. [Exercises and Challenges](#exercises-and-challenges)
7. [Glossary](#glossary)

---

## Introduction to Python

Python is a high-level, beginner-friendly programming language created by Guido van Rossum in 1991. It is widely used in:

- Web development
- Data science and analysis
- Artificial intelligence
- Game development
- Automation and scripting

### Why Learn Python?

| Benefit | Description |
|---------|-------------|
| Easy to read | Python uses simple English-like syntax |
| Versatile | Used in many industries and applications |
| Large community | Lots of help and resources available |
| In-demand skill | Many job opportunities for Python developers |

---

## Setting Up Python

### Step 1: Download Python

1. Go to [python.org](https://python.org)
2. Click "Downloads"
3. Download the latest version for your operating system
4. Run the installer

> **Important:** Tick the box that says "Add Python to PATH" during installation!

### Step 2: Choose a Code Editor

Recommended editors for beginners:

- **IDLE** - Comes with Python (simplest option)
- **Visual Studio Code** - Free and powerful
- **Thonny** - Designed for beginners
- **PyCharm** - Professional IDE

### Step 3: Test Your Installation

Open a terminal or command prompt and type:

```bash
python --version
```

You should see something like: `Python 3.12.0`

---

## Level 1 - Foundation

### 1.1 Your First Python Program

```python
print("Hello, World!")
```

**Explanation:** The `print()` function displays text on the screen. Text must be inside quotation marks.

### 1.2 Variables

Variables are containers that store data.

```python
# Storing text (strings)
name = "Sarah"
school = "City College"

# Storing numbers (integers)
age = 16
year_group = 11

# Storing decimal numbers (floats)
height = 1.65
price = 9.99

# Displaying variables
print(name)
print(age)
```

**Naming Rules:**
- Start with a letter or underscore
- Can contain letters, numbers, and underscores
- Cannot contain spaces
- Case-sensitive (`Name` and `name` are different)

### 1.3 Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text/String | `"Hello"` |
| `int` | Whole number | `42` |
| `float` | Decimal number | `3.14` |
| `bool` | True or False | `True` |

```python
# Check the type of a variable
name = "Alex"
print(type(name))  # Output: <class 'str'>

number = 100
print(type(number))  # Output: <class 'int'>
```

### 1.4 Basic Input and Output

```python
# Getting input from the user
name = input("What is your name? ")
print("Hello, " + name + "!")

# Getting a number from the user
age = input("How old are you? ")
age = int(age)  # Convert text to a number
print("Next year you will be", age + 1)
```

### 1.5 Basic Arithmetic

```python
a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Modulus (remainder): 1
print(a ** b)  # Power: 1000
```

### 1.6 Simple If Statements

```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Key Points:**
- Use a colon `:` after the condition
- Indent the code inside the if/else blocks (use 4 spaces or Tab)

---

## Level 2 - Intermediate

### 2.1 More Complex Conditions

```python
# Using elif (else if)
score = 75

if score >= 90:
    grade = "Distinction"
elif score >= 70:
    grade = "Merit"
elif score >= 50:
    grade = "Pass"
else:
    grade = "Refer"

print("Your grade is:", grade)
```

### 2.2 Comparison and Logical Operators

**Comparison Operators:**

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal | `a >= b` |
| `<=` | Less than or equal | `a <= b` |

**Logical Operators:**

```python
age = 16
has_permission = True

# AND - both conditions must be true
if age >= 16 and has_permission:
    print("You can go on the trip")

# OR - at least one condition must be true
if age < 13 or age > 65:
    print("You get a discount")

# NOT - reverses the condition
if not has_permission:
    print("Permission denied")
```

### 2.3 Loops

**For Loops:**

```python
# Loop through a range of numbers
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with start and end
for i in range(1, 11):
    print(i)  # Prints 1 to 10
```

**While Loops:**

```python
# Repeat while a condition is true
count = 0
while count < 5:
    print(count)
    count = count + 1

# User input validation
password = ""
while password != "secret123":
    password = input("Enter password: ")
print("Access granted!")
```

### 2.4 Lists

Lists store multiple items in a single variable.

```python
# Creating a list
students = ["Alice", "Bob", "Charlie", "Diana"]

# Accessing items (index starts at 0)
print(students[0])   # Alice
print(students[2])   # Charlie
print(students[-1])  # Diana (last item)

# Modifying lists
students.append("Eve")      # Add to end
students.insert(1, "Frank") # Insert at position
students.remove("Bob")      # Remove by value
students.pop(0)             # Remove by index

# List length
print(len(students))

# Check if item exists
if "Alice" in students:
    print("Alice is in the class")
```

### 2.5 Functions

Functions are reusable blocks of code.

```python
# Defining a function
def greet(name):
    print("Hello, " + name + "!")

# Calling a function
greet("Sarah")
greet("James")

# Function with return value
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total)  # 8

# Function with default parameter
def greet_student(name, course="Computing"):
    print(f"Welcome {name} to {course}")

greet_student("Alex")                    # Uses default
greet_student("Jordan", "Business")      # Custom value
```

### 2.6 String Methods

```python
message = "Hello, World!"

print(message.upper())       # HELLO, WORLD!
print(message.lower())       # hello, world!
print(message.replace("World", "Python"))  # Hello, Python!
print(message.split(","))    # ['Hello', ' World!']
print(len(message))          # 13

# String formatting (f-strings)
name = "Alex"
age = 17
print(f"My name is {name} and I am {age} years old")
```

### 2.7 Dictionaries

Dictionaries store data in key-value pairs.

```python
# Creating a dictionary
student = {
    "name": "Emma",
    "age": 17,
    "course": "BTEC Computing",
    "grades": [85, 90, 78]
}

# Accessing values
print(student["name"])       # Emma
print(student.get("age"))    # 17

# Adding/modifying entries
student["email"] = "emma@school.co.uk"
student["age"] = 18

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## Level 3 - Advanced

### 3.1 File Handling

```python
# Writing to a file
with open("data.txt", "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")

# Reading from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open("data.txt", "a") as file:
    file.write("This is a new line\n")
```

### 3.2 Exception Handling

```python
# Basic try-except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Program finished")
```

### 3.3 Object-Oriented Programming (OOP)

**Classes and Objects:**

```python
class Student:
    # Constructor method
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.grades = []

    # Method to add a grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Method to calculate average
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # String representation
    def __str__(self):
        return f"{self.name} ({self.course})"

# Creating objects
student1 = Student("Alice", 17, "Computing")
student2 = Student("Bob", 18, "Business")

# Using methods
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

print(student1)                    # Alice (Computing)
print(student1.get_average())      # 84.33...
```

**Inheritance:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}")

class BTECStudent(Person):
    def __init__(self, name, age, level, course):
        super().__init__(name, age)  # Call parent constructor
        self.level = level
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm studying Level {self.level} {self.course}")

# Using inheritance
student = BTECStudent("Sarah", 17, 3, "Computing")
student.introduce()
# Output:
# Hi, I'm Sarah
# I'm studying Level 3 Computing
```

### 3.4 Working with JSON

```python
import json

# Python dictionary to JSON
student_data = {
    "name": "Alex",
    "age": 17,
    "courses": ["Computing", "Business"],
    "enrolled": True
}

# Write to JSON file
with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

# Read from JSON file
with open("student.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"])
```

### 3.5 List Comprehensions

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension (shorter)
squares = [x ** 2 for x in range(10)]

# With condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

# Filtering a list
names = ["Alice", "Bob", "Anna", "Charlie", "Andrew"]
a_names = [name for name in names if name.startswith("A")]
print(a_names)  # ['Alice', 'Anna', 'Andrew']
```

### 3.6 Modules and Packages

```python
# Importing built-in modules
import random
import datetime
import math

# Random numbers
print(random.randint(1, 100))    # Random int between 1-100
print(random.choice(["a", "b", "c"]))  # Random choice

# Date and time
today = datetime.date.today()
print(today)
print(today.strftime("%d/%m/%Y"))

# Math functions
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(math.ceil(4.3))   # 5
print(math.floor(4.7))  # 4

# Import specific functions
from random import randint, choice
print(randint(1, 10))
```

### 3.7 Working with APIs

```python
import requests
import json

# Making a GET request
response = requests.get("https://api.example.com/data")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# Making a POST request
new_data = {"name": "Alex", "age": 17}
response = requests.post(
    "https://api.example.com/users",
    json=new_data,
    headers={"Content-Type": "application/json"}
)
```

---

## Exercises and Challenges

### Level 1 Exercises

1. **Hello Name** - Write a program that asks for the user's name and says hello to them.

2. **Simple Calculator** - Create a program that asks for two numbers and displays their sum.

3. **Age Checker** - Write a program that asks for the user's age and tells them if they can vote (18+).

4. **Temperature Converter** - Convert Celsius to Fahrenheit using the formula: `F = (C × 9/5) + 32`

### Level 2 Exercises

1. **Times Tables** - Create a program that prints the times table for any number (1-12).

2. **Shopping List** - Build a program where users can add items to a list, view the list, and remove items.

3. **Password Generator** - Generate a random password of a specified length.

4. **Quiz Game** - Create a multiple-choice quiz with at least 5 questions and keep track of the score.

5. **Grade Calculator** - Input multiple grades and calculate the average, then assign a grade (Distinction/Merit/Pass/Refer).

### Level 3 Exercises

1. **Student Management System** - Create a class-based system to manage student records with add, edit, delete, and search functionality.

2. **File-based To-Do App** - Build a to-do list application that saves tasks to a file.

3. **API Data Fetcher** - Fetch data from a public API (e.g., weather, jokes) and display it nicely.

4. **Bank Account Simulator** - Create classes for BankAccount with deposit, withdraw, and transfer methods. Include error handling.

5. **Data Analysis Project** - Read data from a CSV file, perform analysis (averages, max, min), and generate a report.

---

## Glossary

| Term | Definition |
|------|------------|
| **Algorithm** | A step-by-step procedure for solving a problem |
| **Boolean** | A data type with only two values: True or False |
| **Class** | A blueprint for creating objects |
| **Comment** | Text in code that is ignored by Python (starts with #) |
| **Concatenation** | Joining strings together |
| **Condition** | An expression that evaluates to True or False |
| **Dictionary** | A collection of key-value pairs |
| **Float** | A number with a decimal point |
| **Function** | A reusable block of code that performs a task |
| **IDE** | Integrated Development Environment (code editor) |
| **Indentation** | Spaces at the beginning of a line to define code blocks |
| **Index** | The position of an item in a list (starts at 0) |
| **Integer** | A whole number without decimals |
| **Iteration** | Repeating a process (looping) |
| **List** | An ordered collection of items |
| **Loop** | Code that repeats until a condition is met |
| **Method** | A function that belongs to an object |
| **Module** | A file containing Python code that can be imported |
| **Object** | An instance of a class |
| **Parameter** | A variable in a function definition |
| **Return** | Sending a value back from a function |
| **String** | A sequence of characters (text) |
| **Syntax** | The rules for writing valid Python code |
| **Variable** | A named container for storing data |

---

## Useful Resources

- **Official Python Documentation:** [docs.python.org](https://docs.python.org)
- **W3Schools Python Tutorial:** [w3schools.com/python](https://w3schools.com/python)
- **Codecademy:** [codecademy.com](https://codecademy.com)
- **Python Tutor (Visualiser):** [pythontutor.com](https://pythontutor.com)

---

## Tips for Success

1. **Practice regularly** - Code a little bit every day
2. **Type the code yourself** - Don't just copy and paste
3. **Make mistakes** - Errors are how you learn
4. **Read error messages** - They tell you what went wrong
5. **Break problems down** - Solve one small piece at a time
6. **Comment your code** - Future you will thank present you
7. **Ask for help** - Teachers, classmates, and online forums
8. **Build projects** - Apply what you learn to real problems

---

*Document created for BTEC Computing Workshop*
*Last updated: January 2026*
