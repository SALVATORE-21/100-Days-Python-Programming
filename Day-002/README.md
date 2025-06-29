# 🧮 Python Data Types, Math & Type Handling

## 🔡 Subscripting Strings

Subscripting allows you to access individual characters in a string using indexing.

```python
print("Hello"[0])  # Output: H
```

- Indexing starts from 0.

---

## 🔗 String Concatenation

```python
print("123" + "456")  # Output: 123456
```

- Adds the strings, not the numbers.
- This is **concatenation**, not mathematical addition.

---

## 🔢 Integers

```python
print(123456)     # Outputs a number
print(123 + 456)  # Output: 579
```

### 🧱 Large Integers
Python allows underscores `_` in large numbers to make them more readable:

```python
num = 123_456_789
print(num)  # Output: 123456789
```

---

## 🔣 Other Data Types

- **Float**: Decimal numbers like `3.1415`
- **Boolean**: `True` (1), `False` (0)

```python
print(True)   # Output: True
print(False)  # Output: False
```

---

## 🧪 Type Checking

Use the `type()` function to identify the datatype:

```python
print(type(123))       # <class 'int'>
print(type(123.45))    # <class 'float'>
print(type(True))      # <class 'bool'>
print(type("Arya"))    # <class 'str'>
```

---

## 🔁 Type Conversion

Convert between types using:
- `int()`
- `float()`
- `str()`
- `bool()`

### ✅ Valid Example:
```python
a = int("123")
print(type(a))  # <class 'int'>
```

### ❌ Invalid Example:
```python
b = int("abc")  # ValueError: invalid literal for int() with base 10
```

---

## ➗ Mathematical Operations

| Operator | Description         | Example     | Result      |
|----------|---------------------|-------------|-------------|
| `/`      | Division (float)    | `5 / 3`     | `1.6666...` |
| `//`     | Floor Division      | `5 // 3`    | `1`         |
| `*`      | Multiplication      | `5 * 3`     | `15`        |
| `+`      | Addition            | `5 + 3`     | `8`         |
| `-`      | Subtraction         | `5 - 3`     | `2`         |
| `**`     | Power/Exponent      | `5 ** 3`    | `125`       |

---

## 🔢 Order of Operations (PEMDAS)

Python evaluates expressions using this priority:
```
() > ** > * or / > + > -
```

### 🧮 Example:
```python
result = 3 * 3 + 3 / 3 - 3
# Step-by-step:
# = 9 + 1 - 3
# = 10 - 3
# = 7
```

---

## 🎯 Rounding

Use `round(number, decimal_places)` to round float numbers.

```python
round(3.14159, 2)  # Output: 3.14
```

---

## 🧮 Assignment Operators

You can simplify operations using compound assignments:

```python
a = a + 1   # Same as:
a += 1
```

Other examples: `-=`, `*=`, `/=`, `//=`, `**=`

---

## ✨ f-Strings (Formatted Strings)

An `f-string` allows you to embed expressions inside string literals.

```python
name = "Arya"
city = "Delhi"

print(f"Myself is {name} and I live in {city}")
```

- Output: `Myself is Arya and I live in Delhi`

---

## ✅ Summary

- Subscripting accesses characters in a string.
- Use `type()` to check and convert datatypes.
- Python supports math, rounding, and clean formatting with `f-strings`.
- Use readable formatting like underscores in large numbers.
- Mastering data types and operations builds a strong foundation in Python. 🚀🐍
