# Why Python?
- **Beginner-friendly** and easy to learn.
- **Open-source** (free to use and distribute, even commercially).
- **Multi-platform** (Windows, Mac, Linux).
- **Large, supportive community**.
- **Extensive libraries** supporting diverse applications (web development, data science, machine learning).
- **Highly popular language**.

## Downloading Python:
1. Go to [python.org/downloads](https://www.python.org/downloads) or Google it.
2. Download the appropriate version for your OS (Windows, Mac).
3. **Windows Installation:**
   - Run the downloaded executable.
   - **Important:** Add Python to PATH during installation.
   - Verify installation by opening PowerShell and typing `python --version`.

## Creating a Python Project:
1. Create a new project. Python should be selected.
2. Name the project (e.g., "Python Basics").
3. A virtual environment (VENV) will be created. This isolates project dependencies.
4. A default `.py` file might be created – you can delete it.

## Hello World Program:
1. Right-click the project root folder.
2. Create a new Python file named `hello_world.py` (the `.py` extension is added automatically).
3. Use the `print()` function:
   - Type `print("hello world")`. Use tab-completion in the IDE.
4. Run the file by right-clicking and selecting "Run". The output should appear in the console.

## Comments in Python:
- Use `#` for single-line comments. Anything after `#` is ignored by the interpreter.
- Use triple double quotes (`"""comment"""`) for multi-line comments.



# Data Types in Python

## Numbers
### Integers
- Whole numbers (e.g., 2)
### Floats
- Decimal numbers (e.g., 5.50)

## Strings
- Characters and text (e.g., "t-shirt")

## Booleans
- True or False values

---

### Why Data Types? ##
- **Example: Online t-shirt purchase:**
  - **String:** Item description
  - **Integer:** Quantity of t-shirts
  - **Float:** Price and total cost
  - **Boolean:** Checkout confirmation (True/False)

---

## Numbers in Python ##
- Integers and floats are distinct object types.
- Use the `type()` function to determine the type of a number.
- Math operators: `+`, `-`, `*`, `/`, `%` (modulo).
  - Modulo operator (`%`) returns the remainder of a division.
  - Good practice to include spaces around operators for readability.

---

## Strings in Python ##
- Created using single or double quotes.
- Strings are sequences of Unicode characters.
- Access characters by index (starting from 0).
  - Negative indexing accesses characters from the end (e.g., -1 is the last character).
- `len()` function returns the length of a string.

---

## Boolean Values in Python ##
- `True` or `False` (capitalized).
- `type()` returns `bool`.
- Equality operators: `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`.
  - Operators compare values and return a Boolean result.
  - Comparisons must be within the same object hierarchy (e.g., numbers can be compared to numbers, but not directly to strings).
  - `len()` can be used to make strings comparable to numbers.

---

## Truthy and Falsy ##
- `bool()` function converts values to Booleans.
  - Numbers: 0 is false, any other number is true.
  - Strings: Empty strings are false, non-empty strings are true.
- Truthy/falsy values are useful for conditional logic (e.g., checking if a form field is empty).
---
# Python Concepts

## Python Variables
- Variables store data types and objects in reserved memory locations.
- Created by assigning a name (e.g., A) followed by an equals sign and a value (e.g., `A = 5`).
- `print(A)` displays the variable's value.
- `type(A)` returns the variable's data type.
- Variables are like named boxes for organizing data in code.
- **Variable Naming Rules:**
  - Cannot start with a literal (number, string, boolean).
  - Use underscores for multi-word names (e.g., `my_variable`).
  - Spaces in names cause errors.
- Variables are mutable (can be changed). Overwriting a variable replaces its previous value.

---

## String Concatenation
- Joining strings using the `+` operator.
- Need to explicitly add spaces between strings.
- Cannot directly concatenate strings and other data types (e.g., integers).
- Use `str()` to cast other data types to strings before concatenation.

---

## String Escaping
- Use backslashes (`\`) to escape special characters within strings, such as quotes.
  - This allows quotes to be treated as literal characters.

---

## String Methods
- Built-in functions to manipulate strings.
- Examples:
  - `capitalize()`: Capitalizes the first character.
  - `upper()`: Converts the entire string to uppercase.
  - `replace()`: Replaces characters within a string.
- Many more methods available (search online for "Python string methods").

---

## Control Flow (if statements)
- `if` keyword evaluates a condition (using equality operators).
- Code within the `if` block executes only if the condition is true.
- Colons (`:`) mark the beginning of indented code blocks.
- Indentation is crucial in Python; it defines code block boundaries.
- `elif` (else if) handles multiple conditions sequentially. Only the first true condition's block is executed.
- `else` provides a default block if no conditions are met.

---

## Logical Operators
- `and`: Both conditions must be true for the entire condition to be true.
- `or`: Only one condition needs to be true for the entire condition to be true.
- Can chain multiple conditions together. Keep it simple for readability.

---
# Collections in Python
- Enable storing large amounts of data in specific formats, unlike basic data types (strings, numbers) which have a one-to-one relationship with variables.
- Two main collection types covered: lists and dictionaries.

---

## Lists
- Similar to arrays in other languages.
- Ordered, mutable sequences of items.
- Can contain any data type (strings, numbers, booleans, even other lists).
- Index-based, starting from zero. Negative indexing is supported (e.g., -1 for the last item).
- Accessed using square brackets and the index (e.g., `example_list[0]`).
- Can store multiple data types, but recommended to keep lists homogeneous for real-world applications.
- **Methods:**
  - `append()`: Adds an item to the end of the list.
  - `pop()`: Removes and returns the last item (or a specific item by index).
  - `index()`: Returns the index of a specific item.

---

## Dictionaries
- Similar to hash maps in other languages.
- Unordered collections of key-value pairs.
- Keys are typically strings (camel case or dashes recommended), but can be other immutable types. Values can be any data type.
- Accessed using square brackets and the key (e.g., `contact_list["John Doe"]`).
- Created using curly braces `{}`.
- Key-value pairs separated by colons `:`.
- Adding new key-value pairs or modifying existing ones is done by assigning a value to a key (e.g., `contact_list["Jane Doe"] = "555-1234"`).
- **Methods:**
  - `keys()`: Returns a view of all keys.
  - `values()`: Returns a view of all values.
  - `pop()`: Removes and returns the value associated with a specific key.

---

## Nested Dictionaries
- Dictionaries can contain other dictionaries as values, allowing for complex data structures (e.g., a contact list with nested dictionaries for each contact containing name, phone number, etc.).
- Accessing nested elements is done by chaining square bracket lookups (e.g., `contact_list["B"]["phone"]`).

# Python Loops
- Loops allow actions to be applied to each object within a collection. Two loop types: `while` and `for`.

---

## While Loops
- Relies on boolean conditions; operates only if the condition is true.
- Requires careful management of the condition to avoid infinite loops.
- **Loop control variable:** A variable used to control the loop's condition.
- **Increment operators:** `+=`, `-=`, `*=`, `/=`, etc. (e.g., `counter += 1`)
- Can be combined with `if` statements inside the loop.

### Example While Loop:
```python
counter = 0
while counter < 10:
    print(counter)
    if counter % 2 == 0:
        print(counter)  # Prints even number itself.
    else:
        print("Odd number")
    counter += 1
```
---
# For Loops:
- Iterates over an **iterable object** (e.g., list, string, dictionary).
- **Placeholder variable**: Represents each item in the iterable during each iteration.
- **`in` keyword**: Used to iterate through the sequence.

## Iterable Objects:
- **Lists**
- **Strings** (treated as a list of characters)
- **Dictionaries** (keys by default, values accessible via `.values()` method)

## Example For Loops:

### String:
```python
my_string = "hello"
for character in my_string:
    print(character)
```
**Example 2**
```python
customers = {"name": "Alice", "city": "New York"}
for customer in customers:  # Iterates through keys
    print(customer)

for value in customers.values(): # Iterates through values
    print(value)
```
---
# Functions in Python:
- Enable **modular coding** by breaking down code into smaller, reusable blocks.
- This promotes **organization** and avoids repetition, adhering to the **DRY** (Don't Repeat Yourself) principle.

## Creating a Function:
1. Use the `def` keyword followed by the function name (e.g., `print_name`).
2. Add parentheses `()` after the function name, which will contain any arguments.
3. End the line with a colon `:`.
4. Indent the code block belonging to the function.

## Calling a Function:
- Execute the function by writing its name followed by parentheses.

## Arguments:
- Make functions **dynamic** by passing arguments within the parentheses.
- Use relevant argument names (e.g., `first_name`).
- Access arguments within the function body using their names.
- Multiple arguments can be passed, separated by commas.
- Arguments are mandatory; if a function expects an argument, it must be provided.

## Return Keyword:
- Functions often return a value using the `return` keyword.
- This allows the function's output to be used elsewhere in the program.
- A function with a `return` statement doesn't automatically print the returned value; you need to explicitly print it if desired.

## Example: `full_name` and `print_name` functions:
- The `full_name` function takes `first_name` and `last_name` as arguments, concatenates them, and returns the full name string.
- The `print_name` function takes a data type (e.g., the output of `full_name`) as an argument and prints it.

## Key Takeaway:
- Functions promote **code reusability** and **organization**. They often take data, process it, and return a result to be used by other parts of the program.
