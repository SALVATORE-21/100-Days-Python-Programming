# 🔍 Python Conditionals & Logic

## 🧠 `if` Statements — Conditional Logic

Conditional statements allow Python to make decisions based on certain conditions.

### 📌 Basic Structure:
```python
if condition:
    # do this
else:
    # do this instead
```

### 🎢 Example: Roller Coaster Ride Eligibility
```python
print("Welcome to the roller coaster ride")
height = int(input("What is your height: "))

if height > 120:
    print("You can ride")
else:
    print("You cannot ride")
```

---

## 🔢 Comparison Operators

| Operator | Meaning                    |
|----------|----------------------------|
| `==`     | Equal to                   |
| `!=`     | Not equal to               |
| `>`      | Greater than               |
| `<`      | Less than                  |
| `>=`     | Greater than or equal to   |
| `<=`     | Less than or equal to      |
| `=`      | Assignment (not comparison)|

---

## ➗ Modulo Operator: `%`

The modulo operator returns the **remainder** after division.

```python
10 % 5   # Output: 0
10 % 3   # Output: 1
```

### 🧮 Example: Even or Odd Checker
```python
num = int(input("Enter a number to check if it's even or odd: "))
if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")
```

---

## 🧱 Nested `if` / `elif` / `else`

You can place an `if` inside another `if` to check multiple levels of conditions.

### 🎫 Example: Age-based Ticket Price
```python
age = int(input("Enter your age: "))
if age < 12:
    print("You need to pay $5")
elif 12 < age < 18:
    print("You need to pay $7")
else:
    print("You need to pay $12")
```

---

## 🎯 Special Multi-Check Conditions

Multiple `if` blocks (not chained with `elif`) allow **multiple conditions** to be checked and executed independently.

### 🎢 Full Roller Coaster Logic with Offers & Add-ons:
```python
print("Welcome to the roller coaster ride")
height = int(input("What is your height: "))

if height > 120:
    print("You can ride")
    age = int(input("Enter your age: "))

    if age < 12:
        bill = 5
        print("You need to pay $5")
    elif 12 <= age < 18:
        bill = 7
        print("You need to pay $7")
    elif 45 <= age <= 55:
        print("You can have a free ride on us!")
        bill = 0
    else:
        bill = 12
        print("You need to pay $12")

    want_photo = input("Do you want a photo? Type 'y' for yes, 'n' for no: ")
    if want_photo == 'y':
        print("You need to pay $3 for the photo")
        bill += 3

    print("The final bill is:", bill)
else:
    print("You cannot ride")
```

---

## 🔗 Logical Operators in Python

| Operator | Description                           | Example                          |
|----------|---------------------------------------|----------------------------------|
| `and`    | All conditions must be `True`         | `if a > 10 and b < 20`           |
| `or`     | At least one condition must be `True` | `if a > 10 or b < 20`            |
| `not`    | Inverts the truth value               | `if not is_logged_in`            |

### 🧠 Examples:
```python
if age > 18 and height > 120:
    print("Eligible")

if age < 12 or age > 60:
    print("You get a discount!")

if not is_member:
    print("Please register")
```

---

## ✅ Summary

- Use `if`, `elif`, and `else` to control the program’s decisions.
- Modulo `%` helps in checking divisibility (like even/odd).
- Nested and multiple `if` blocks allow deeper logic.
- Logical operators (`and`, `or`, `not`) make conditions more powerful.

Mastering conditional logic is key to writing intelligent and dynamic Python programs! 🚀🐍
