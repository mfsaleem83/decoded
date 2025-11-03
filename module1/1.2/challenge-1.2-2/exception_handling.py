"""
## Challenge: Add Error Handling to a Script

**Goal:** Practice using `try` / `except` blocks to catch and handle common errors in Python.

Review the common built-in exceptions in Python in the table below (https://docs.python.org/3/library/exceptions.html)

| Exception               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `SyntaxError`           | Raised when the parser encounters a syntax error                           |
| `NameError`             | Raised when a variable is not found in the local or global scope           |
| `TypeError`             | Raised when an operation is applied to an object of inappropriate type     |
| `ValueError`            | Raised when a function receives an argument of the right type but wrong value |
| `IndexError`            | Raised when a sequence index is out of range                               |
| `KeyError`              | Raised when a dictionary key is not found                                  |
| `AttributeError`        | Raised when an attribute reference or assignment fails                     |
| `ImportError`           | Raised when an import statement fails to find the module                   |
| `ModuleNotFoundError`   | Subclass of `ImportError` for when the module itself cannot be found       |
| `ZeroDivisionError`     | Raised when a number is divided by zero                                    |
| `FileNotFoundError`     | Raised when a file or directory is requested but doesn’t exist             |
| `IOError`               | Raised when an input/output operation fails                                |
| `RuntimeError`          | Raised when an error is detected that doesn't fall in any other category   |
| `NotImplementedError`   | Raised to indicate that a method or function hasn’t been implemented yet   |
| `AssertionError`        | Raised when an `assert` statement fails                                    |


Review the following code which asks the user for a number, divides 100 by it and prints the result:

```python
user_input = input("Enter a number: ")
number = int(user_input)
result = 100 / number
print("Result is:", result)
```

Refactor the code by adding error handling to:

- Catch invalid input e.g. if the user types `"hello"` instead of a number (hint: `ValueError`)
- Prevent a crash if the user types `0` (hint: `ZeroDivisionError`)
- Display a helpful message in each case
- *Stretch:*
    - Add a `finally:` block that prints `"Finished processing input."` whether or not there was an error.
    - Wrap this in a function called `safe_divide()` and call it.
"""


def safe_divide():
    print("Finished processing input.")


user_input = input("Enter a number: ")
try:
    number = int(user_input)
    result = 100 / number
    print("Result is:", result)
except TypeError as ve:
    print("You can only user numbers")
except ZeroDivisionError as zd:
    print("0 is not divisible. Please select another number")
finally:
    safe_divide()
