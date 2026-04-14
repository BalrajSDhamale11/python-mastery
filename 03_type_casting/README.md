# 🔄 Concept 03: Type Casting

> **Core Idea:** Converting one data type into another.
> Critical because `input()` ALWAYS returns a string — no matter what the user types.

---

## 🧠 Key Concepts Covered
- `int()`, `float()`, `str()`, `bool()` conversion functions
- Why `input()` always returns `str`
- Choosing the right cast for the right situation
- Chaining methods: `input().strip().lower()`
- f-string decimal formatting: `{value:.2f}`

---

## 💡 Golden Rules
- `input()` always returns `str` — cast immediately, every time
- Use `float` over `int` for user numbers when decimals are possible
- `int("3.5")` throws an ERROR — can't cast decimal string to int directly
- Chain your operations: `float(input("Enter: ").strip())`
- Reflex: number from user → wrap in `float()` or `int()` instantly

---

## 📝 Problems Solved

### Level 1 — The Age Calculator
Take birth year as input, calculate approximate age using current year.

**Key skill:** Casting `input()` to `int` for math operations

```
Enter your birth year: 2004
Your age is approximately: 22
```

**Key line:**
```python
birth_year = int(input("Enter your birth year: "))
```

---

### Level 2 — The Strict Calculator
Take two numbers, print sum, difference, product, division. Handle division by zero.

**Key skill:** Choosing `float` over `int` for a calculator. Division by zero check (used if/else early!)

```
Enter first number: 10
Enter second number: 3

Sum        : 13.0
Difference : 7.0
Product    : 30.0
Division   : 3.3333333333333335
```

**Why float over int?**
- `int("3.5")` → ERROR
- `int(3.5)` → 3 (loses decimal)
- `float` handles all number inputs safely

---

### Level 3 — The Data Type Converter
Take one float input and convert it to all 4 types, printing each result.

**Key skill:** Float as the safest base type. Understanding what each cast does.

```
Enter a number: 7.9

As int   : 7       ← truncates decimal
As float : 7.9     ← unchanged
As str   : "7.9"   ← becomes text
As bool  : True    ← non-zero = True
```

---

## 🔑 The Casting Cheat Sheet
```python
int("20")       # "20"  → 20
int(3.9)        # 3.9   → 3    (truncates, doesn't round)
float("8.5")    # "8.5" → 8.5
float(5)        # 5     → 5.0
str(100)        # 100   → "100"
bool(0)         # 0     → False
bool("")        # ""    → False
bool("hello")   # "hello" → True
```

---

## 🔑 The :.2f Format
```python
x = 3.14159
print(f"{x:.2f}")   # 3.14
print(f"{x:.4f}")   # 3.1416
print(f"{x:.0f}")   # 3
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3