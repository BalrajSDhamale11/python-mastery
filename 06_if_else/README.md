# 🔀 Concept 06: if / else

> **Core Idea:** Your program making decisions.
> Variables store data. Math processes data. **if/else decides what to DO with data.**
> This is where programs stop being calculators and start being intelligent.

---

## 🧠 Key Concepts Covered
- `if`, `elif`, `else` structure
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`
- Condition ordering — why sequence matters
- Input validation — checking before processing
- Comparison chaining: `0 <= x <= 100`
- Short-circuit evaluation

---

## 💡 Golden Rules
- Indentation is NOT style in Python — it IS syntax. Missing it = crash.
- `=` assigns. `==` compares. Confusing these is the #1 beginner bug.
- **Bouncer rule:** The moment one condition is True — Python stops checking the rest.
- Always check validity BEFORE processing — invalid input should never reach logic.
- Condition order matters — check most specific/restrictive first.
- Wrap grade/processing logic in `else` after validation — so invalid input never gets processed.

---

## 📝 Problems Solved

### Level 1 — The Age Gate
Categorize a person by age into Child, Teenager, Adult, or Senior Citizen.

**Key skill:** `if/elif/elif/else` structure. Top-down condition ordering.

```
Enter your age: 25
You are an Adult.
```

**Smart ordering — highest first:**
```python
if age >= 60:      # Senior first
elif age >= 18:    # Adult
elif age >= 13:    # Teenager
else:              # Child — everything remaining
```
> No redundant conditions needed. Each check implies the previous failed.

---

### Level 2 — The Smart Login System
Validate username and password against stored credentials. 3 distinct outcomes.

**Key skill:** Condition ordering logic. `.lower()` on username, NOT on password.

```
✅ Login Successful! Welcome, raj.
❌ Username not found.
⚠️ Wrong password. Try again.
```

**Why check username first?**
```python
if username == stored and password == stored:  # both correct
elif username != stored:                        # wrong username
elif password != stored:                        # username right, password wrong
```
> If username is wrong — password doesn't matter.
> Checking password first would give wrong user a "wrong password" message — a security leak.

---

### Level 3 — The Smart Grade Calculator
Full grade report with validation. Student name, 3 subjects, average, grade, remark.

**Key skill:** Input validation + grade logic. Three ways to validate — all discovered independently.

```
===== Grade Report for Raj =====
Subject 1  : 85.0
Subject 2  : 72.0
Subject 3  : 90.0
Average    : 82.33
Grade      : B
Remark     : Good Performance
================================
```

**Grading system:**
```python
if average >= 90:     # A — Excellent!
elif average >= 80:   # B — Good Performance
elif average >= 70:   # C — Average Performance
elif average >= 60:   # D — Needs Improvement
else:                 # F — Please Work Harder
```

---

## 🔑 Three Validation Approaches (All Valid)

```python
# Approach 1 — Explicit or conditions (straightforward)
if subject_1 < 0 or subject_1 > 100 or subject_2 < 0 or ...:

# Approach 2 — Comparison chaining (cleanest)
if not (0 <= subject_1 <= 100 and 0 <= subject_2 <= 100 and 0 <= subject_3 <= 100):

# Approach 3 — List + any() (most scalable — works for any number of subjects)
marks = [subject_1, subject_2, subject_3]
if any(m < 0 or m > 100 for m in marks):
```
> Approach 3 is what professional code looks like.
> You'll understand it fully after Lists + Comprehensions.

---

## 🔑 The Validation + Logic Pattern
```python
if invalid_input:
    print("Invalid.")
else:
    # ALL processing goes here
    # Invalid data NEVER reaches this block
```
> Always validate first. Always process inside else.
> Invalid input reaching logic = bugs in real systems.

---

## 🔑 Comparison Operators
```python
==   # equal to
!=   # not equal to
>    # greater than
<    # less than
>=   # greater or equal
<=   # less or equal
```

## 🔑 Logical Operators
```python
and  # both must be True
or   # at least one must be True
not  # flips True to False, False to True
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3