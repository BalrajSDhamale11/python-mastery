# 🔗 Concept 07: Logical Operators

> **Core Idea:** Combining multiple conditions into one decision.
> Every real system — bank approvals, app permissions, game rules — is just
> `and`, `or`, `not` conditions underneath.

---

## 🧠 Key Concepts Covered
- `and`, `or`, `not` operators
- Truth tables — knowing outputs cold
- Short-circuit evaluation
- Operator precedence: `not > and > or`
- De Morgan's Law
- Pre-computing conditions into named variables
- Specific-before-general condition ordering

---

## 💡 Golden Rules
- Pre-compute conditions into named variables — code reads like English
- Check most **specific** condition first — "too young AND too short" before "too young"
- Use brackets when combining `and`/`or` — never assume precedence
- `not (A or B)` == `not A and not B` — De Morgan's Law
- Short circuit: `False and anything` → False instantly. `True or anything` → True instantly.
- Separate decision logic from display logic — store results in variables, print after

---

## 📝 Problems Solved

### Level 1 — The Amusement Park Entry
Multi-condition entry checker — age, height, and parent permission combined.

**Key skill:** Pre-computing conditions. Specific-before-general ordering. Bool input handling.

```python
has_permission = input("Has parent permission? (True/False): ").strip() == "True"
is_tall_enough = height >= 140
is_old_enough  = age >= 12
is_adult       = age >= 18

if is_tall_enough and is_old_enough and (is_adult or has_permission):
    print("✅ Entry Allowed!")
elif not is_old_enough and not is_tall_enough:   # specific first
    print("❌ Too young and too short.")
elif not is_old_enough:
    print("❌ Too young for this ride.")
elif not is_tall_enough:
    print("❌ Too short for this ride.")
elif not is_adult and not has_permission:
    print("❌ Need parent permission.")
```

---

### Level 2 — The Loan Eligibility Checker
Bank loan approval with standard and high-income relaxed credit rules.

**Key skill:** Modeling rule exceptions. Condition ordering by elimination speed.

```python
eligible_age = age >= 21
eligible_monthly_income = monthly_income >= 25000
eligible_credit_score = credit_score >= 700
eligible_credit_score_relaxed = credit_score >= 600
high_income = monthly_income > 50000

if high_income and eligible_credit_score_relaxed and eligible_age:
    print("✅ Loan Approved — high income approval")
elif eligible_age and eligible_credit_score and eligible_monthly_income:
    print("✅ Loan Approved — standard approval")
elif not eligible_age:
    print("❌ Not Eligible — too young")
elif not eligible_monthly_income:
    print("❌ Not Eligible — insufficient income")
else:
    print("❌ Not Eligible — credit score too low")
```

---

### Level 3 — The Smart Ticket Booking System
Cinema pricing with age categories, Tuesday discount, and member discount.

**Key skill:** Layered decision making. Guard conditions. Discount initialized to 0 defensively.

```
===== 🎬 Ticket Summary for Raj =====
Age          : 28
Category     : Adult
Base Price   : ₹250
Tuesday Disc : -₹50.00
Member Disc  : -₹50.00
Final Price  : ₹150.00
=====================================
```

**Key pattern — defensive initialization:**
```python
tuesday_discount = 0.0   # initialized before logic
member_discount  = 0.0   # safe even if conditions never trigger

if base_price > 0:       # one guard — handles free tickets elegantly
    if is_tuesday:
        tuesday_discount = base_price * 0.20
    if is_member:
        member_discount = 50.0

final_price = base_price - tuesday_discount - member_discount
```

---

## 🔑 Truth Tables

**`and`:**
```
True  and True  → True
True  and False → False
False and True  → False
False and False → False
```

**`or`:**
```
True  or True  → True
True  or False → True
False or True  → True
False or False → False
```

**`not`:**
```
not True  → False
not False → True
```

---

## 🔑 De Morgan's Law
```python
not (A or B)   ==  not A and not B
not (A and B)  ==  not A or not B
```

**Example:**
```python
# These are identical:
if not (is_adult or has_permission):
if not is_adult and not has_permission:
```

---

## 🔑 Operator Precedence
```python
not > and > or

# Always use brackets when mixing and/or:
True or False and False      # → True or (False and False) → True
(True or False) and False    # → True and False → False
```

---

## 🔑 Bool Input Pattern
```python
# Clean way to take bool input from user:
is_member = input("Are you a member? (True/False): ").strip().lower() == "true"
# Returns actual bool True or False — not a string
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3