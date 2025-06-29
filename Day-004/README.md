# 🎲 Python Randomisation & Lists

## 🌪️ What is Randomisation?

Randomisation is the occurrence of a **random event** from a set of possible outcomes — in other words, dealing with **probability**.

### 🔧 Required Module:
```python
import random
```

### 🧪 Common Random Functions:

| Function | Description |
|----------|-------------|
| `random.randint(a, b)` | Returns a random **integer** between `a` and `b` (inclusive). |
| `random.random()` | Returns a random **float** between `0.0` and `1.0`. |
| `random.random() * 10` | Float between `0` and `10`. |
| `random.uniform(a, b)` | Float between `a` and `b`, inclusive. |
| `random.choices(list, k=n)` | Picks `n` random items from a list. |
| `random.shuffle(list)` | Shuffles items of a list in-place. |
| `random.choice(list)` | Picks a single random item from the list. |

---

## 🪙 Heads or Tails Game

### 💡 Coin Flip Example:
```python
import random

Heads_or_tail = random.randint(0, 1)
if Heads_or_tail == 0:
    print("Heads")
else:
    print("Tails")
```

---

## 📦 Python Lists - The Basics

Lists in Python are powerful **data structures** used to store and organize data.

### ✅ Key Characteristics:
1. A list can hold **multiple data types**:
   ```python
   ["hello", 123, 3.14, True]
   ```
2. Lists are **ordered** and support **indexing** (starts from 0).
3. Support **negative indexing**:
   ```python
   a = [1, 2, 3, 4]
   print(a[-1])  # Output: 4
   ```
4. Lists are **mutable**, meaning items can be modified.

---

## 🛠️ List Operations & Methods

| Function | Description |
|----------|-------------|
| `list.append(x)` | Adds item `x` to the **end** of the list. |
| `list.extend([x, y])` | Adds multiple items to the list. |
| `list.insert(i, x)` | Inserts item `x` at index `i`. |
| `list.remove(x)` | Removes the first occurrence of `x`. |
| `list.pop([i])` | Removes item at index `i` (defaults to last item). |
| `list.clear()` | Removes all items from the list. |
| `random.choice(list)` | Picks a random item from the list. |

---

## 🔚 Summary

- **Randomisation** helps simulate real-world unpredictability.
- **`random` module** gives tools to generate integers, floats, and shuffle/pick items.
- **Lists** are flexible, mutable data containers with powerful built-in methods.

Keep experimenting with random and list operations to build games, simulations, and more! 🧠💻
