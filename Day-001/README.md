# 🧵 Python String Operations, Input & Variables

## 🧑‍💻 String Operations in Python

Strings are sequences of characters and are one of the most fundamental data types in Python.

---

## 📥 New Line in Strings

Use `\n` to insert a newline in a string.

```python
print("Hi myself is Arya\nI am 22 yrs old")
```

### 🖨️ Output:
```
Hi myself is Arya
I am 22 yrs old
```

---

## 🔗 String Concatenation

You can **combine** strings using the `+` operator.

```python
print("shashank" + "arya")        # Output: shashankarya
print("shashank" + " " + "Arya")  # Output: shashank Arya
```

- ⚠️ **Spaces matter** in Python — they are not added automatically.
- Always include `" "` if you want a space between words.

---

## 🧑‍⚖️ Indentation Matters

Python uses **indentation** (spaces/tabs at the beginning of a line) to define **code blocks**.
Improper indentation will raise an error — it's critical for syntax.

---

## 🎙️ Taking User Input

### 📌 Basic Input Example:
```python
print("What is your name?")
name = input()  # Takes input from user
print(f"Henceforth, your identity is considered as: {name}")
```

### 🧠 One-line Input Usage:
```python
print("You are " + input("What is your age: ") + "!")
```

- This line first asks for age and then prints the message in one go.

---

## 🧮 Finding Length of a String

Use the `len()` function to get the length (number of characters) in a string:

```python
print("The length of the name is:", len(name))
```

---

## 📦 Variables

### 💡 What is a Variable?

A **variable** is a **named container** used to store data for future reference and reuse.

```python
user_name = "Arya"
print("Welcome", user_name)
```

- You assign values using `=`
- Variables help you reuse information throughout your program.

---

## ✅ Summary

- Use `+` for string concatenation; add spaces manually when needed.
- Use `\n` to break lines within strings.
- `input()` is used for interactive user input.
- `len()` returns the length of a string.
- Variables store reusable data and are a core concept in any program.

Mastering these basics sets you up for building dynamic Python applications. 🐍💬
