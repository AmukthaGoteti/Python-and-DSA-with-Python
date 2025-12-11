### I. Python Fundamentals

#### A. Keywords
Python keywords define the **rules and structure** of Python programs. They **cannot be used as identifiers** (names of variables, functions, or classes). Attempting to use a keyword as a variable will result in a Syntax Error.
Keywords can be categorized by function, including:
*   **Value Keywords:** `True`, `False`, `None`.
*   **Operator Keywords:** `and`, `or`, `not`, `is`, `in`.
*   **Control Flow Keywords:** `if`, `else`, `elif`, `for`, `while`, `break`, `continue`, `pass`, `try`, `except`, `finally`, `raise`, `assert`.
*   **Function and Class Keywords:** `def`, `return`, `lambda`, `yield`, `class`.
*   **Scope and Name Space Keywords:** `global`, `nonlocal`.

#### B. Variables and Literals
A **variable** is a container or storage data area used to hold data. Python is a **dynamically typed language**, meaning you do not explicitly define the variable type. **Literals** are the representation of fixed values in a program and are often used to assign values to variables or constants.

**Numeric Literals** are immutable (unchangeable) and can be integers, floats, or complex numbers. **String literals** are text wrapped inside quotation marks (single or double).

#### C. Python Operators
Operators are special symbols used to perform operations on variables and values.

| Operator Type | Description | Example Operators |
| :--- | :--- | :--- |
| **Arithmetic** | Used for basic mathematical operations (addition, subtraction, multiplication, division). | `+`, `-`, `*`, `/`, `//` (Floor Division), `%` (Modulus), `**` (Exponentiation). |
| **Relational (Comparison)** | Compares values and returns either `True` or `False` based on the condition. | `>`, `<`, `>=`, `<=`, `==` (checks equality), `!=`. |
| **Logical** | Used to combine conditional statements. | `AND`, `OR`, `NOT`. |
| **Bitwise** | Acts on bits and performs bit-by-bit operations on binary numbers. | `&`, `|`, `^`, `~`, `>>`, `<<`. |
| **Assignment** | Used to assign values to variables. | `=`, `+=`, `-=`, `*=`. |
| **Identity** | Checks if two values are located on the same part of memory. | `is`, `is not`. |
| **Membership** | Tests whether a value or variable is in a sequence. | `in` (True if value is found), `not in` (True if value is not found). |

**Ternary operators** (also known as conditional expressions) evaluate something based on a condition being `True` or `False`.

### II. Input and Output

#### A. The `print()` Function
The `print()` function is used to print a Python object(s) to the standard output.
The general syntax is `print(object(s), sep, end, file, flush)`.

The function can also be used to:
1.  Print multiple objects separated by a specified value using the `sep` argument.
2.  Print the contents of an external file using the `open()` and `read()` functions, and directing the output to `sys.stderr` by importing the `sys` package and using `file=sys.stderr` in the print function.

#### B. Output Formatting
Output formatting manages how data is presented, making information more understandable.

1.  **String Modulo Operator (`%`):** This is one of the oldest ways to format strings, allowing you to embed values within a string using **format specifiers** (e.g., `%d` for decimal, `%f` for floating point, `%s` for string).
2.  **`format()` Method:** This provides a more flexible way to handle string interpolation by using curly braces `{}` as placeholders. It supports both **positional** (indexed placeholders like `{0}`) and **named** arguments. The `format()` method also supports detailed formatting options like setting widths, alignment, and precision.
3.  **String Alignment Methods:** Methods like `str.center()`, `str.ljust()`, and `str.rjust()` provide straightforward ways to format strings by aligning them within a specified width.

#### C. The `input()` Function
The `input()` function is used to take input from the user. By default, `input()` always returns data as a **string**. If other types (like integer or float) are needed, **typecasting** must be used (e.g., `int(input(...))` or `float(input(...))`). Multiple values can be taken on a single line separated by spaces using the `.split()` method.

### III. Control Flow and Loops

#### A. If-Else Statements
An **`if` statement** executes a block of code only when a specified condition is satisfied. Python uses **indentation** to define a block of code within the `if` statement.
The **`if-else` statement** includes an optional `else` clause that executes if the condition in the `if` statement evaluates to `False`.
For multiple conditions, the **`if-elif-else`** structure is used to execute a block of code among several alternatives. It is also possible to have **nested `if` statements** (an `if` statement inside another `if` statement).

#### B. The `range()` Function
The `range()` function returns a **sequence of numbers** in a given range.
It can be initialised in three ways:
1.  **`range(stop)` (1 argument):** Generates numbers starting at 0, up to (but not including) `stop`.
2.  **`range(start, stop)` (2 arguments):** Generates numbers from `start` up to (but not including) `stop`.
3.  **`range(start, stop, step)` (3 arguments):** Allows setting the `start`, `stop`, and the increment/decrement value (`step`).

**Note:** The `range()` function **does not support floating-point numbers**; its arguments must be integers. Concatenating the results of two `range()` functions (integer numbers) can be achieved using the `chain()` method from `itertools`. The sequence returned by `range()` supports both positive and negative indexing.

#### C. Loops (`for` and `while`)
1.  **`for` loop:** Used to **iterate over sequences** such as lists, strings, and dictionaries. Python uses indentation to define the block of code (body of the loop). If you iterate through a string, you get individual characters. The `range()` function is often used to iterate for a fixed number of times.
2.  **`while` loop:** Used to **repeat a block of code until a certain condition is met**. If the condition always evaluates to `True`, it forms an **infinite loop**.

#### D. Loop Control Statements
*   **`break` statement:** Used to **alter the flow of loops**; it terminates the `for` loop (or `while` loop) immediately before it iterates through all items, exiting the loop entirely.
*   **`continue` statement:** Skips the current iteration of the loop and proceeds to the next iteration.

### IV. Functions and Object-Oriented Programming (OOP)

#### A. Python Functions
A function is a block of code that performs a specific task, making the program easier to understand and reuse.

*   **Definition and Calling:** Functions are defined using `def`. Creating a function definition means the code is ready for use, but to execute it, you must **call the function**.
*   **Arguments and Return:** **Arguments** are inputs given to the function. The **`return` statement** denotes that the function has ended and returns a value; any code after `return` is not executed.
*   **`pass` statement:** Serves as a placeholder for future code, preventing errors from empty code blocks. It is typically used when code is planned but not yet written.
*   **Built-in Functions:** Python provides several built-in functions that can be used directly. Library functions like `sqrt()` (square root) and `pow()` (power of a number) are defined inside modules (e.g., `math`) and must be imported to be used.

#### B. Object-Oriented Programming (OOP) Concepts
Python supports OOP through the use of objects and classes.
*   **Object:** Any entity that has **attributes** (data like name, age, color) and **behaviours** (actions like dancing, singing).
*   **Class:** A **blueprint** for the object.

The key features of OOP include:
1.  **Inheritance:** A way of creating a **new class (derived/child class)** using details of an **existing class (base/parent class)** without modifying the existing class.
2.  **Encapsulation:** Refers to the bundling of attributes and methods inside a single class. It prevents outer classes from accessing and changing private attributes, thus achieving **data hiding**. In Python, private attributes are denoted using a single or double underscore prefix (e.g., `_maxprice` or `__maxprice`).
3.  **Polymorphism:** Simply means "more than one form," where the same entity can perform different operations in different scenarios.

### V. Pattern Programs
Pattern programs involve sequences of characters or numbers arranged in a way that resembles a pyramid, with each level typically having one more element than the level above.

The detailed notes include functions and examples for printing various pyramid and pattern types, often implemented using nested loops and the `range()` function:

*   Full Pyramid pattern (using nested `for` loops for spaces and asterisks).
*   Number Pyramid (prints numbers).
*   Inverted Full Pyramid Pattern.
*   Hollow Pyramid.
*   Half Pyramid Pattern (both iterative and recursive implementations shown).
*   Pattern of Numbers (incrementing the number sequentially).
*   Pattern of Alphabets (using ASCII values, initialized to 65 for 'A').
*   Inverted Half Pyramid Pattern.
*   Hollow Inverted Half Pyramid.
