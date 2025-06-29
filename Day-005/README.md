# 🔐 Why We Get Pwned & Mastering Python Loops

## 💥 Reason for Getting Pwned!!
Many online accounts get **compromised (pwned)** due to weak password practices.
**Key Mistake:** Using the **same password** across multiple platforms.

### ✅ Recommendation:
- Always use **unique passwords** for every account.
- Consider using a password manager for better security.
- Strong passwords = Stronger digital life!

---

## 🔁 Python `for` Loops - Mastering Iteration

The `for` loop in Python allows you to iterate over sequences like lists, tuples, or ranges.

### 🍎 Example: Iterating through a list of fruits

```python
fruits = ["Apple", "Orange", "Grapes"]
for i in fruits:
    print(i)
```

📌 **Output:**
```
Apple
Orange
Grapes
```

---

## 🏆 Finding the Maximum Value in a List

### ✅ Using the built-in `max()` function:
```python
student_scores = [56, 89, 91, 73]
print(max(student_scores))
```

### 🔄 Using a `for` loop to find the max:
```python
student_scores = [56, 89, 91, 73]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print("MAX_SCORE:", max_score)
```

---

## ➕ Summing Numbers from 1 to 100

### 📌 Using `range()` and a loop:
```python
SUM = 0
for i in range(1, 101):
    SUM += i
print("The sum of 100 numbers is:", SUM)
```

### 🧠 Explanation of `range()`:
- `range(a, b)` returns values from `a` to `b-1`
- `range(a, b, c)` steps by `c`
  - Example: `range(0, 11, 2)` → 0, 2, 4, 6, 8, 10

---

## 🚀 Summary

- **Passwords:** Never reuse them. Strengthen your digital safety.
- **For Loops:** Powerful for iterating over data.
- **Range:** Useful for generating sequences of numbers.
- **Hands-on Practice:** Essential to master logic and patterns.

Keep coding. Stay secure. 💻🔒
