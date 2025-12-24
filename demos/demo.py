# demo.py - Python Code Snippet for Theme Preview
# pylint: disable=all


# Multiline Comments
"""
This is a multiline comment.
It can span multiple lines.
"""

# Variables and Data Types
# Python 3.10+
integer_var: int = 10
float_var: float = 3.14159
string_var: str = "Hello, world!"
boolean_var: bool = True
list_var: list[int | str | float] = [1, 2, 3, "four", 5.0]
tuple_var: tuple[int, str, float] = (1, "two", 3.0)
dictionary_var: dict[str, str | int] = {"key1": "value1", "key2": 2}
set_var: set[int] = {1, 2, 3}
none_var: None = None

# Python 3.9 and below (using Union)
from typing import Dict, List, Set, Tuple, Union

list_var: List[Union[int, str, float]] = [1, 2, 3, "four", 5.0]
tuple_var: Tuple[int, str, float] = (1, "two", 3.0)
dictionary_var: Dict[str, Union[str, int]] = {"key1": "value1", "key2": 2}
set_var: Set[int] = {1, 2, 3}

r"\n"
b"hello"

# String Formatting
name = "John"
age = 30

# f-strings (Python 3.6+)
formatted_string_f = f"Hello, my name is {name} and I am {age} years old."

# str.format()
formatted_string_format = "Hello, my name is {} and I am {} years old.".format(name, age)

# % operator
formatted_string_percent = "Hello, my name is %s and I am %d years old." % (name, age)

# Operators
a = 10
b = 5
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulo = a % b
exponentiation = a**b

# Walrus Operator (Python 3.8+)
if (n := len(string_var)) > 10:
    print(f"String is longer than 10 characters: {n}")

# Control Flow
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

for i in range(5):
    print(i)

while a > 0:
    print(a)
    a -= 1

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")
    raise RuntimeError from e  # Raise from the original exception
finally:
    print("This always executes")

with open("file.txt", "w") as f:
    f.write("Hello from Python!")


# Functions
def greet(name: str) -> None:
    print(f"Hello, {name}!")


greet("World")


# Function with variable positional arguments
def sum_numbers(*args: int) -> int:
    total = 0
    for num in args:
        total += num
    return total


result = sum_numbers(1, 2, 3, 4, 5)
print(f"Sum: {result}")


# Function with variable keyword arguments
def print_details(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="John", age="30", city="New York")


# Function with positional-only arguments (Python 3.8+)
def greet_positional(name: str, /, greeting: str = "Hello") -> None:
    print(f"{greeting}, {name}!")


greet_positional("John")  # Valid
greet_positional(name="John")  # Invalid


# Classes
class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self) -> None:
        print("Woof!")


my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()

# Modules and Packages
import math
import random
from datetime import datetime

print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.now())


# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()


# Generators
def my_generator(n: int):
    for i in range(n):
        yield i


for i in my_generator(5):
    print(i)

# List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)

# Lambda Functions
add = lambda x, y: x + y
print(add(5, 3))

# Asynchronous Programming (Python 3.5+)
import asyncio


async def my_coroutine():
    print("Starting coroutine")
    await asyncio.sleep(1)
    print("Ending coroutine")


asyncio.run(my_coroutine())


# Type Hints (Python 3.5+)
def greeting(name: str) -> str:
    return f"Hello, {name}"


# Context Managers
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContextManager() as manager:
    print("Inside context")

# Data Classes (Python 3.7+)
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


point = Point(10, 20)
print(point)

# Match-Case (Python 3.10+)
status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not found")
    case _:
        print("Unknown status")

# Assert
assert 2 + 2 == 4, "Math is broken!"

# Global and Nonlocal
global_var = 10


def modify_global():
    global global_var
    global_var = 20


modify_global()
print(global_var)  # Output: 20


def outer_function():
    nonlocal_var = 10

    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var = 20

    inner_function()
    print(nonlocal_var)  # Output: 20


outer_function()
