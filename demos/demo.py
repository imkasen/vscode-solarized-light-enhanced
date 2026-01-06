import asyncio
import sys
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Callable, Optional, Union

# ----------------------------------------------------------------------------
# 1. Literals, Variables & Built-ins
# ----------------------------------------------------------------------------

# Constants (Naming convention)
MAX_RETRIES = 5
TIMEOUT = 30.5

# Numeric Literals
integer_val = 42
float_val = 3.14_159  # Underscore separator
hex_val = 0xFF_00_AA
binary_val = 0b1010_0011
complex_val = 10 + 5j

# String Literals
simple_str = "Single quoted"
double_str = "Double quoted"
docstring = """
    Multi-line string (Docstring).
    Often highlighted differently than normal strings.
"""
bytes_literal = b"Bytes data"
raw_string = r"Raw \n string"

# F-Strings (Python 3.6+)
name = "World"
# Debugging f-string (Python 3.8+)
formatted = f"Hello {name}, {integer_val=}, Result: {float_val:.2f}"

# Built-in Constants
flag_true = True
flag_false = False
nothing = None

# ----------------------------------------------------------------------------
# 2. Modern Type Hints (Python 3.10/3.12+)
# ----------------------------------------------------------------------------

# Type Alias Statement (Python 3.12+)
type Point = tuple[float, float]
type Vector[T] = list[T]  # Generic type alias

# Old style type hint
StringList = list[str]  # Python 3.9+ lowercase generics

# ----------------------------------------------------------------------------
# 3. Functions, Arguments & Decorators
# ----------------------------------------------------------------------------

def log_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Simple decorator example."""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Positional-only args (/) and Keyword-only args (*)
@log_decorator
def complicated_args(p1: int, p2: int, /, standard: int, *, kw1: bool = True) -> int:
    """
    Shows Python 3.8+ syntax for argument separators.
    """
    result = p1 + p2 + standard
    return result if kw1 else 0

# Generator
def range_generator(n: int):
    i = 0
    while i < n:
        yield i
        i += 1

# Lambda
square = lambda x: x**2

# ----------------------------------------------------------------------------
# 4. Classes & Object Oriented
# ----------------------------------------------------------------------------

class Status(Enum):
    IDLE = auto()
    RUNNING = auto()
    ERROR = auto()

@dataclass
class User:
    id: int
    username: str
    _password: str = "secret"  # Protected convention

    # Magic Methods (Dunder methods)
    def __str__(self) -> str:
        return self.username

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id

class Admin(User):
    def __init__(self, id: int, username: str, level: int):
        super().__init__(id, username)
        self.level = level

    @property
    def is_super(self) -> bool:
        return self.level > 10

    @is_super.setter
    def is_super(self, val: bool):
        pass

# ----------------------------------------------------------------------------
# 5. Control Flow & Pattern Matching (Python 3.10+)
# ----------------------------------------------------------------------------

def process_command(command: Union[str, tuple]):
    # Structural Pattern Matching
    match command:
        case "start" | "go":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case ["move", x, y] if isinstance(x, int):  # Guard clause
            print(f"Moving to ({x}, {y})")
        case {"action": action, "value": val}:
            print(f"Action: {action}, Value: {val}")
        case _:
            print("Unknown command")

def logical_flow():
    # Walrus Operator (Python 3.8+)
    data = [1, 2, 3]
    if (n := len(data)) > 2:
        print(f"List is long: {n} items")

    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except (ValueError, TypeError):
        pass
    else:
        print("Success")
    finally:
        print("Cleanup")

    # Exception Groups (Python 3.11+)
    try:
        raise ExceptionGroup("Group", [ValueError("A"), TypeError("B")])
    except* ValueError:
        print("Caught ValueErrors")
    except* TypeError:
        print("Caught TypeErrors")

# ----------------------------------------------------------------------------
# 6. Async / Await (Asynchronous Programming)
# ----------------------------------------------------------------------------

async def fetch_data(url: str) -> dict:
    await asyncio.sleep(0.1)
    return {"data": "sample"}

async def main():
    async with asyncio.Lock():
        result = await fetch_data("http://example.com")

    # Async iterator
    # async for item in async_generator(): pass

if __name__ == "__main__":
    logical_flow()
