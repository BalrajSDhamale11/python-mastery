# 🔤 Concept 04: String Methods

> **Core Idea:** Built-in tools Python gives you to manipulate and examine text.
> String methods are your most used tools in real projects — forms, databases, user input.

---

## 🧠 Key Concepts Covered
- Core string methods: `upper()`, `lower()`, `title()`, `capitalize()`
- Cleaning methods: `strip()`, `lstrip()`, `rstrip()`
- Search methods: `find()`, `count()`, `startswith()`, `endswith()`
- Modification: `replace()`
- Splitting: `split()`
- `len()` for string length
- Method chaining: `input().strip().lower()`

---

## 💡 Golden Rules
- String methods do NOT change the original — they return a NEW value
- Save the result if you need it: `name = name.upper()`
- `.strip()` on every input — users always add accidental spaces
- `find()` returns `-1` when nothing is found — not `False`, not `0`
- Golden rule: `if condition: x = True else: x = False` → collapse to `x = condition`
- `.lower()` on username inputs — not on passwords (passwords are case sensitive)

---

## 📝 Problems Solved

### Level 1 — The Name Formatter
Take full name input and print in 4 formats with length.

**Key skill:** Core formatting methods + `len()`

```
Enter your full name: raj sharma

Original   : raj sharma
Uppercase  : RAJ SHARMA
Lowercase  : raj sharma
Title Case : Raj Sharma
Length     : 10
```

---

### Level 2 — The Input Cleaner
Clean a messy email and username. Validate underscore, check prefix, calculate length.

**Key skill:** Chaining methods, using boolean results directly, real-world input cleaning

```
Cleaned Email    : raj.sharma@gmail.com
Cleaned Username : raj_2004
Has underscore   : True
Starts with raj  : True
Email length     : 20
```

**3 ways to check for underscore:**
```python
# Way 1 — direct bool (cleanest)
has_underscore = '_' in username

# Way 2 — count
has_underscore = username.count('_') > 0

# Way 3 — find
has_underscore = username.find('_') != -1
```

---

### Level 3 — The Message Formatter
Full message analysis — clean, format, count words, search, replace.

**Key skill:** Combining all string methods. Self-learned `split()` and `:.2f` formatting.

```
===== Message Report =====
Original        :    hello world, my name is raj!
Cleaned         : hello world, my name is raj!
Uppercase       : HELLO WORLD, MY NAME IS RAJ!
Word Count      : 6
Contains 'raj'  : True
Starts with 'hello' : True
Ends with 'raj!'    : True
Replace 'raj' → 'amit' : hello world, my name is amit!
==========================
```

---

## 🔑 Methods Cheat Sheet
```python
s = "  Hello World  "

s.upper()           # "  HELLO WORLD  "
s.lower()           # "  hello world  "
s.strip()           # "Hello World"
s.title()           # "  Hello World  "
s.replace("Hello", "Hi")  # "  Hi World  "
s.find("World")     # 8  (index) — -1 if not found
s.count("l")        # 3
s.startswith("  H") # True
s.endswith("  ")    # True
s.split()           # ["Hello", "World"]
len(s)              # 15
```

---

## 🔑 The Golden Rule
```python
# ❌ Unnecessary
if '_' in username:
    has_underscore = True
else:
    has_underscore = False

# ✅ Clean
has_underscore = '_' in username
```
> Whenever `if condition: x = True else: x = False` — collapse it.

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3