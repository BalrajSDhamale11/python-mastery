# 📦 Concept 01: Variables

> **Core Idea:** A variable is a named box that stores a value.
> Mastering variables means mastering how data is held, moved, and preserved in your program.

---

## 🧠 Key Concepts Covered
- Declaring and assigning variables
- Using variables in print statements
- f-strings for clean output
- Swapping values using a temp variable
- Data preservation during operations

---

## 💡 Golden Rules
- Name variables like labels on real boxes — `name` not `x`
- Never hardcode values in print — always use variables
- Write logic in English **before** writing code
- Python convention: always use `snake_case` for variable names

---

## 📝 Problems Solved

### Level 1 — Digital Visiting Card
Store your name, age, city, and hobby in variables and print a clean visiting card.

**Key skill:** Variable declaration + f-string printing

```
Name   : Raj
Age    : 20
City   : Pune
Hobby  : Football
```

---

### Level 2 — Swap Without Looking
Swap two variables `a = "Morning"` and `b = "Evening"` using a temp variable. Print before and after states.

**Key skill:** Temp variable logic — understanding data preservation

```
Before Swap:        After Swap:
a = Morning         a = Evening
b = Evening         b = Morning
```

**Why temp?**
Without temp — `a = b` overwrites `a`. Now both hold `"Evening"`.
When you then do `b = a` — you're just copying `"Evening"` back.
Temp saves the original before it gets overwritten.

---

### Level 3 — The Profile Swap
Swap complete profiles (name AND age) of two users. Two separate swaps, two temp variables.

**Key skill:** Multiple independent swaps — knowing when one temp isn't enough

```
--- Before Swap ---       --- After Swap ---
User1 : Arjun, Age 22    User1 : Sara, Age 25
User2 : Sara, Age 25     User2 : Arjun, Age 22
```

---

## 🔑 Concept That Unlocks Later
```python
# Python one-line swap (Tuple Unpacking — learned in Tuples)
a, b = b, a
```
You used the temp method intentionally — it trains logic thinking.
The one-liner will make full sense once you learn Tuples.

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3