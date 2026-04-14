# 🔢 Concept 05: Math Functions

> **Core Idea:** Python's built-in and module-based tools for mathematical operations.
> Used in finance, science, games, data — everywhere numbers need processing.

---

## 🧠 Key Concepts Covered
- Built-in math: `round()`, `abs()`, `max()`, `min()`, `pow()`
- `import math` module: `sqrt()`, `ceil()`, `floor()`, `pi`
- Banker's Rounding — Python's `round()` quirk
- Three ways to square a number
- `:.2f` f-string formatting for decimal control
- Real-world application: bill splitting, BMI, unit conversion

---

## 💡 Golden Rules
- `import math` always goes at the TOP of your file
- `math.ceil()` always rounds UP — even on negatives (toward zero)
- `math.floor()` always rounds DOWN — even on negatives (away from zero)
- `round()` uses Banker's Rounding — `.5` rounds to nearest EVEN number
- Use `float` inputs for any calculator — handles decimals safely
- `**` is the most Pythonic way to do powers: `height ** 2`

---

## 📝 Problems Solved

### Level 1 — The Math Toolbox
Demonstrate all math functions with user inputs. Separated built-in vs module functions with comments.

**Key skill:** Knowing which functions need `import math` and which don't

```
rounded_value  = 4.0
absolute_value = 7.3
raised_value   = 125.0
max_value      = 9.2
min_value      = 3.1
square_root    = 7.0
ceil_value     = 8
floor_value    = 7
pi_value       = 3.141592653589793
```

---

### Level 2 — The Bill Splitter
Calculate bill split with tip percentage. Three rounding options per person.

**Key skill:** Real-world math logic — tip calculation, per-person split, rounding choices

```
===== Bill Split =====
Bill Amount  : 850.0
Tip Amount   : 85.0
Total + Tip  : 935.0
Each Pays    : 311.67
Each Pays↑   : 312      ← ceil — no one underpays
Each Pays↓   : 311      ← floor
======================
```

**Tip calculation:**
```python
tip_amount = (total_bill * tip_percentage) / 100
# OR cleaner:
tip_amount = total_bill * (tip_percentage / 100)
```

---

### Level 3 — The BMI Calculator (With Unit Conversion)
Full BMI calculator with kg/lb and m/ft conversion. Self-added feature — unprompted.

**Key skill:** Combining all math tools. Product thinking — handling real user inputs.

```
===== BMI Report for Raj =====
Weight : 70.00 kg
Height : 1.75 m
BMI    : 22.86
Ceiling BMI  : 23
Floor BMI    : 22
Absolute diff: 0.14
==============================
```

---

## 🔑 Three Ways To Square
```python
height = 1.75

height ** 2           # 3.0625 — most Pythonic ✅
pow(height, 2)        # 3.0625 — built-in
math.pow(height, 2)   # 3.0625 — always returns float
```

---

## 🔑 Banker's Rounding — Python's Quirk
```python
round(2.5)   # 2 ← rounds to nearest EVEN
round(3.5)   # 4 ← rounds to nearest EVEN
round(4.5)   # 4 ← rounds to nearest EVEN
round(5.5)   # 6 ← rounds to nearest EVEN
```
> Python rounds `.5` to the nearest **even** number — not always up.
> This is mathematically correct and avoids bias in large datasets.
> Used in finance and data science.

---

## 🔑 ceil/floor On Negatives
```python
math.ceil(-7.3)   # -7  ← rounds UP (toward zero)
math.floor(-7.3)  # -8  ← rounds DOWN (away from zero)
```
> Most beginners flip these on negatives. Remember:
> ceil = UP always. floor = DOWN always. Direction doesn't change.

---

## 🔑 Decimal Formatting
```python
x = 3.14159
print(f"{x:.2f}")   # 3.14
print(f"{x:.4f}")   # 3.1416
print(f"{x:.0f}")   # 3
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3