# String Methods in Python

Python has a variety of built-in string methods that make it easier working and manipulating text data. Here are some of the most commonly used string methods and example of how to use.

## 1. str.upper()

- It converts all the characters to uppercase.

  ```python
  text = "Hey!"
  result = text.upper()
  ```


## 2. str.lower()

- It converts all characters in a string to lowercase.

    ```python
    text = "Hello, World!"
    result = text.lower()
    ```
    

## 3. str.strip()

- It removes leading and trailing whitespace from a string.
    
    ```python
    text = "   Hello, World!  "
    result = text.strip()
    ```
## 4. str.replace(old, new)

- It replaces all occurrences of a specified substring with another substring.

    ```python
    text = "Hello, World!"
    result = text.replace("Hello", "Hi")
    ```

## 5. str.split(delimiter)

- It splits a string into a list of substrings based on a specified delimiter.

    ```python
    text = "apple,banana,cherry"
    result = text.split(",")
    ```

## 6. str.join(iterable)

- It joins the elements of an iterable into a single string using the specified string as a separator.

    ```python

    fruits = ['apple', 'banana', 'cherry']
    result = ', '.join(fruits)
    ```

## 7. str.startswith(prefix)

- It checks if a string starts with a specified string.

    ```python
    text = "Hello, World!"
    starts_with_hello = text.startswith("Hello")
    ```

## 8. str.endswith(suffix)

- It checks if a string ends with a specified suffix.

    ```python
    text = "Hello, World!"
    ends_with_world = text.endswith("World!")
    ```
