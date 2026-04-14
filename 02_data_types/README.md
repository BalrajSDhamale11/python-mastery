# 🔢 Concept 02: Data Types

> **Core Idea:** Every value in Python has a type.
> Knowing types means knowing what your data IS — and what you can do with it.

---

## 🧠 Key Concepts Covered
- The 4 core data types: `int`, `float`, `str`, `bool`
- Using `type()` to inspect data
- Truthiness — what Python considers True and False
- The difference between `True` (bool) and `"True"` (str)
- Bool as a subtype of int

---

## 💡 Golden Rules
- `True` and `False` are bool values — `"True"` and `"False"` are just text
- `bool` secretly equals `int` in Python: `True = 1`, `False = 0`
- **Truthiness rule:** Zero = False. Everything else = True
- Empty string `""` = False. Space `" "` = True (it's a character)
- Most bugs come from mixing types — know your types instinctively

---

## 📝 Problems Solved

### Level 1 — Know Your Data
Create variables of all 4 types and print each value alongside its data type using `type()`.

**Key skill:** Recognizing and declaring correct data types

```
Raj      → <class 'str'>
20       → <class 'int'>
8.5      → <class 'float'>
True     → <class 'bool'>
```

---

### Level 2 — The Type Detective
Given 6 variables — predict each one's data type WITHOUT using `type()`, then verify.

**Key skill:** Reading values and identifying types by sight

```python
a = 100      # int
b = "100"    # str   ← quotes make it text
c = 100.0    # float ← decimal makes it float
d = False    # bool
e = "True"   # str   ← quotes make it text, NOT bool
f = 0        # int
```

**The traps:**
- `"True"` looks like bool — it's `str` because of quotes
- `0` looks like False — it's `int`

---

### Level 3 — The Smart Receipt
Build a receipt calculator using all 4 data types. Calculate total from quantity × price.

**Key skill:** Combining types in a real-world program

```
===== QuickMart Receipt =====
Item      : Headphones
Quantity  : 2
Unit Price: 1299.99
Total     : 2599.98
Discount  : True
=========================
```

---

## 🔑 The Truthiness Table
```python
bool(0)      # False — zero
bool(0.0)    # False — zero float
bool("")     # False — empty string
bool(" ")    # True  — space is a character
bool("False")# True  — non-empty string
bool(1)      # True  — non-zero
bool(-5)     # True  — non-zero
bool("hi")   # True  — non-empty
```

---

## 🔑 Bool Is a Subtype of Int
```python
True + 1      # 2
False + 5     # 5
True + True   # 2
True + False  # 1
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3