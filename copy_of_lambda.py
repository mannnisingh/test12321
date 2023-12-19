# -*- coding: utf-8 -*-
"""Copy of Lambda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nL7jDn3ybVyk5VSPZhEzbrGOVXxC1IIS

Ans1.

A lambda function is a small anonymous function defined using the `lambda` keyword. It is also known as a lambda expression. Lambda functions are often used for short-term operations where a full function definition is not necessary. The general syntax of a lambda function is:

```python
lambda arguments: expression
```

Here's a simple example:

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

In this example, the lambda function takes two arguments (`x` and `y`) and returns their sum.

Here are some key differences between lambda functions and regular functions (defined using the `def` keyword):

1. **Anonymous vs Named:**
   - Lambda functions are anonymous, meaning they are not named. They are typically used for short operations and are not meant for reuse across multiple parts of a program.
   - Regular functions are named and can be defined using the `def` keyword. They are generally used for more complex operations and can be reused at different parts of a program.

2. **Syntax:**
   - Lambda functions have a more concise syntax and can only consist of a single expression.
   - Regular functions have a more elaborate syntax and can contain multiple expressions, statements, and even documentation (docstrings).

3. **Scope of Variables:**
   - Lambda functions can only reference variables in their own scope and the global scope. They cannot modify variables from the enclosing scope.
   - Regular functions can access variables from their own scope, the global scope, and any enclosing scopes. They can also modify variables from these scopes using the `global` and `nonlocal` keywords.

4. **Return Statement:**
   - Lambda functions implicitly return the result of the expression.
   - Regular functions use the `return` statement to explicitly return a value. They can have multiple `return` statements.

In general, lambda functions are suitable for simple, one-time operations, while regular functions are more appropriate for larger, reusable pieces of code. The choice between them depends on the specific requirements of a given task.

Ans.2

Yes, a lambda function in Python can have multiple arguments. The syntax for a lambda function with multiple arguments is similar to that of a regular function. Here's the general syntax:

```python
lambda argument1, argument2, ..., argumentN: expression
```

Here's an example of a lambda function with two arguments:

```python
multiply = lambda x, y: x * y
print(multiply(3, 5))  # Output: 15
```

In this example, the lambda function takes two arguments, `x` and `y`, and returns their product.

You can extend this pattern to include as many arguments as needed. Here's an example with three arguments:

```python
add_three_numbers = lambda x, y, z: x + y + z
print(add_three_numbers(2, 4, 6))  # Output: 12
```

Lambda functions are particularly useful in situations where you need a quick, one-time function and don't want to go through the process of defining a full function using the `def` keyword. However, for more complex or reusable functions, using `def` to define a regular function might be more appropriate.

Ans3.

Lambda functions in Python are often used in situations where a small, anonymous function is needed for a short duration and where the creation of a full function using `def` would be overly verbose. Lambda functions are commonly employed in functional programming constructs, such as `map`, `filter`, and `sorted`. They are also used in situations where a function is required as an argument to another function.

an example use case where a lambda function is used with the `sorted` function:

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

# Display the sorted list
print(sorted_students)
```

 example, the `sorted` function is used to sort the list of students based on their scores (the second element in each tuple). The `key` parameter is set to a lambda function that extracts the score from each tuple. The `reverse=True` parameter is used to sort the list in descending order.

Lambda functions are also commonly used with functions like `map` and `filter`. Here's an example using `map` to square each element in a list:

```python
numbers = [1, 2, 3, 4, 5]


squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)
```

this lambda function is applied to each element in the `numbers` list using `map`, resulting in a new list of squared numbers.

While lambda functions are powerful and concise for certain use cases, it's essential to consider readability and code maintainability. For more complex or frequently used functions, defining a regular function using `def` may be more appropriate.

Ans.4

Lambda functions in Python have their advantages and limitations compared to regular functions defined using the `def` keyword. Here are some of the key points:

### Advantages of Lambda Functions:

1. **Conciseness:**
   - Lambda functions are more concise than regular functions. They allow you to write short, one-line functions without the need for a full function definition.

2. **Readability in Certain Contexts:**
   - Lambda functions can enhance readability in situations where a short, simple function is used as an argument to higher-order functions (e.g., `map`, `filter`, `sorted`).

3. **No Need for Function Name:**
   - Lambda functions are anonymous, so there's no need to come up with a function name, making them suitable for short-lived and one-time use cases.

4. **Functional Programming:**
   - Lambda functions are often used in functional programming constructs where functions are treated as first-class citizens.

### Limitations of Lambda Functions:

1. **Limited Expressiveness:**
   - Lambda functions are limited to a single expression. They cannot contain statements or multiple expressions, making them unsuitable for more complex logic.

2. **Readability in Complex Cases:**
   - For longer or more complex functions, lambda expressions can reduce code readability. In such cases, using `def` to define a regular function with a meaningful name and a clear structure is often preferred.

3. **No Documentation Strings:**
   - Lambda functions cannot have documentation strings (docstrings), which are useful for documenting the purpose and usage of a function.

4. **Limited Scope of Variables:**
   - Lambda functions have a more restrictive scope. They can only reference variables in their own scope and the global scope. They cannot modify variables from the enclosing scope without using workarounds.

5. **Less Discoverability:**
   - Since lambda functions are anonymous, it might be harder for other developers (or even yourself) to understand their purpose without carefully reading the code.

 lambda functions are a concise and useful tool for specific situations, particularly when working with higher-order functions and simple, short-lived operations. However, for more complex or frequently used functions, regular functions defined with `def` are generally preferred for their readability, expressiveness, and the ability to include documentation. The choice between lambda functions and regular functions depends on the specific requirements and context of the code.

Ans5.

Yes, lambda functions in Python can access variables defined outside of their own scope, but with some limitations. Lambda functions can access variables from their own scope, the global scope, and any enclosing scopes. However, they cannot modify variables from the enclosing scope directly unless those variables are declared as `global` or `nonlocal`.

Here's an example to illustrate:

```python
# Global variable
global_variable = 10

def outer_function():
    outer_variable = 5

    # Lambda function accessing variables from its own scope and the global scope
    lambda_func = lambda x: x + outer_variable + global_variable

    return lambda_func

# Create a lambda function by calling the outer function
my_lambda = outer_function()

# Use the lambda function
result = my_lambda(3)

# Display the result
print(result)  # Output: 18 (3 + 5 + 10)
```

In this example, the lambda function `lambda_func` takes one argument `x` and accesses the `outer_variable` from its own scope and the `global_variable` from the global scope. When the lambda function is called with the argument `3`, it returns the sum of `x`, `outer_variable`, and `global_variable`.

Now, let's modify the example to attempt to modify the `outer_variable` from within the lambda function:

```python
global_variable = 10

def outer_function():
    outer_variable = 5

    # Lambda function attempting to modify a variable from the enclosing scope
    lambda_func = lambda x: outer_variable + x
    # Uncomment the line below to see an error
    # outer_variable += 1

    return lambda_func

my_lambda = outer_function()

# Use the lambda function
result = my_lambda(3)

print(result)
```

If you uncomment the line `# outer_variable += 1`, you will encounter an error. Lambda functions can't modify variables from enclosing scopes directly, so attempting to modify `outer_variable` in this way will result in an `UnboundLocalError`. To modify variables from enclosing scopes, you would need to use the `nonlocal` keyword inside a regular function instead of a lambda function.

Ans.6

create a lambda function to calculate the square of a given number  

```python
square = lambda x: x**2

# Example usage
number = 5
result = square(number)

print(f"The square of {number} is: {result}")
```

In this example, the lambda function `lambda x: x**2` takes a single argument `x` and returns its square. The `result` variable is then assigned the value of the square of the `number` variable, and the result is printed.

Ans7.

Create a lambda function to find the maximum value in a list of integers using the `max` function with a lambda key function

```python
find_max = lambda lst: max(lst)

# Example usage
numbers = [3, 8, 1, 6, 4, 9, 2, 7, 5]
max_value = find_max(numbers)

print(f"The maximum value in the list is: {max_value}")
```

 the lambda function `lambda lst: max(lst)` takes a list (`lst`) as an argument and returns the maximum value using the `max` function. The `max_value` variable is then assigned the result of applying this lambda function to the `numbers` list, and the maximum value is printed.

Ans8.

use the `filter` function along with a lambda function to filter out all the even numbers from a list of integers. Here's an example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Original list:", numbers)
print("Filtered list (keeping only odd numbers):", filtered_numbers)
```

 lambda function `lambda x: x % 2 != 0` is used as the filtering criterion. It returns `True` for odd numbers (those where the remainder after division by 2 is not zero) and `False` for even numbers. The `filter` function is then used to filter the list, and `list()` is used to convert the filtered result into a list. Finally, both the original list and the filtered list are printed.
 output:

```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Filtered list (keeping only odd numbers): [1, 3, 5, 7, 9]
```

Ans9.

Use the `sorted` function with a lambda function as the `key` argument to sort a list of strings based on their length in ascending order.
 example:

```python
strings = ["apple", "banana", "cherry", "date", "elderberry"]

# Use a lambda function with sorted to sort strings based on their length
sorted_strings = sorted(strings, key=lambda x: len(x))

print("Original list:", strings)
print("Sorted list (ascending order based on length):", sorted_strings)
```

 the lambda function `lambda x: len(x)` is used as the key function for sorting. It returns the length of each string, and the `sorted` function uses these lengths to sort the strings. Finally, both the original list and the sorted list are printed.

output:

```
Original list: ['apple', 'banana', 'cherry', 'date', 'elderberry']
Sorted list (ascending order based on length): ['date', 'apple', 'banana', 'cherry', 'elderberry']
```

Ans10.

Use a lambda function with the `filter` function to create a lambda function that takes two lists as input and returns a new list containing the common elements between them. Here's an example:

```python
# Two example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = lambda lst1, lst2: list(filter(lambda x: x in lst1, lst2))

result = common_elements(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", result)
```

output:

```
List 1: [1, 2, 3, 4, 5]
List 2: [3, 4, 5, 6, 7]
Common elements: [3, 4, 5]
```

Ans11.

Factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. Here's an example of a recursive function in Python to calculate the factorial of a given positive integer:

```python
def factorial(n):
   
    if n == 0:
        return 1
   
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)

print(f"The factorial of {number} is: {result}")
```

In this recursive function, the base case is when `n` is equal to 0, in which case the factorial is 1. For any other positive integer `n`, the function recursively calls itself with the argument `(n - 1)` until it reaches the base case.

example usage calculates the factorial of 5, and the result is printed:

```
The factorial of 5 is: 120
```

Ans12

Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence starts with 0 and 1. Here's an example of a recursive function in Python to compute the nth Fibonacci number:

```python
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example
n = 6
result = fibonacci(n)

print(f"The {n}th Fibonacci number is: {result}")
```

recursive function, the base cases are when `n` is 0 or 1, in which case the function returns 0 or 1, respectively. For any other positive integer `n`, the function recursively calls itself with the arguments `(n - 1)` and `(n - 2)` until it reaches the base cases.

example usage calculates the 6th Fibonacci number, and the result is printed:

```
The 6th Fibonacci number is: 8
```

Ans.13

Create a recursive function to find the sum of all elements in a given list. Here's an example in Python

```python
def recursive_sum(lst):
  
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

# Example usage
my_list = [1, 2, 3, 4, 5]
result = recursive_sum(my_list)

print(f"The sum of elements in the list is: {result}")
```

recursive function, the base case is when the list is empty (`not lst`). In this case, the sum is 0. For a non-empty list, the function returns the sum of the first element (`lst[0]`) and the sum of the rest of the elements (`recursive_sum(lst[1:])`), calculated by making a recursive call.

example usage calculates the sum of elements in the list `[1, 2, 3, 4, 5]`, and the result is printed:

```
The sum of elements in the list is: 15
```

Ans14.

Palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward. Here's an example of a recursive function in Python to determine whether a given string is a palindrome

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

# Example usage
word1 = "radar"
word2 = "python"

print(f"Is '{word1}' a palindrome? {is_palindrome(word1)}")
print(f"Is '{word2}' a palindrome? {is_palindrome(word2)}")
```

recursive function, the base case is when the length of the string is 0 or 1, in which case the function returns `True` since an empty string or a string with one character is considered a palindrome. For longer strings, the function checks whether the first and last characters are equal (`s[0] == s[-1]`) and then makes a recursive call on the substring excluding the first and last characters (`is_palindrome(s[1:-1])`).

example usage checks whether the strings "radar" and "python" are palindromes, and the results are printed:

```
Is 'radar' a palindrome? True
Is 'python' a palindrome? False
```

Ans.15

The greatest common divisor (GCD) of two positive integers is the largest positive integer that divides both numbers without leaving a remainder. Here's an example of a recursive function in Python to find the GCD of two positive integers:

```python
def gcd(a, b):
   
    if b == 0:
        return a
    
    else:
        return gcd(b, a % b)

# Example usage
num1 = 48
num2 = 18

result = gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")
```

recursive function, the base case is when the second number (`b`) becomes 0. In this case, the GCD is the first number (`a`). For any other pair of positive integers `(a, b)`, the function returns the GCD of `(b, a % b)`, which is calculated by making a recursive call.

example usage calculates the GCD of 48 and 18, and the result is printed:

```
The GCD of 48 and 18 is: 6
```
"""