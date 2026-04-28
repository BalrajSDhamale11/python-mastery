# 🔄 Concept 09: For Loop

> **Core Idea:** Run a block of code a specific number of times or over every item in a sequence.
> For loops are for KNOWN iterations. While loops are for UNKNOWN iterations.
> This distinction matters every time you choose between them.

---

## 🧠 Key Concepts Covered
- `for` loop with `range()` — start, stop, step
- Looping over strings character by character
- `break` — exit immediately on condition
- `continue` — skip iteration, guard sections without `else`
- `for...else` — fires ONLY when loop completes without `break`
- `enumerate()` — index + value together
- String multiplication: `"* " * n`
- Nested loops — outer controls rows, inner controls columns
- Prime number detection algorithm

---

## 💡 Golden Rules
- `range(1, 11)` = 1 through 10 — stop is always EXCLUDED
- `range(1, n+1)` for inclusive n — muscle memory
- `continue` removes need for `else` — guards the section below it
- `for...else` — the `else` fires only if no `break` occurred
- One loop = one pass — calculate everything you need in that single pass
- Always use variables in output strings — never hardcode dynamic values
- String multiplication: `"* " * 3` → `"* * * "` — cleaner than inner loop sometimes

---

## 📝 Problems Solved

### Level 1 — The Multiplication Table
Print full multiplication table for any number.

**Key skill:** `range(1, 11)`. Calculation inside f-string.

```
===== Multiplication Table of 7 =====
7 x 1  = 7
7 x 2  = 14
...
7 x 10 = 70
======================================
```

```python
number = int(input("Enter a number: "))
print(f"\n===== Multiplication Table of {number} =====")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print("======================================")
```

---

### Level 2 — The Smart Sum Calculator
Calculate total, even, odd sums and counts in ONE loop pass.

**Key skill:** Single pass efficiency. `continue` as a guard. Both approaches documented.

```
===== Summary for 1 to 10 =====
Total Sum   : 55 (count: 10)
Even Sum    : 30 (count: 5)
Odd Sum     : 25 (count: 5)
================================
```

**With `continue` (advanced):**
```python
for i in range(1, n+1):
    total_sum += i
    total_count += 1

    if i % 2 == 0:
        even_sum += i
        even_count += 1
        continue    # guards odd section — no else needed

    # Only reached if number is odd (continue skipped this)
    odd_sum += i
    odd_count += 1
```

**Without `continue` (beginner):**
```python
for i in range(1, n+1):
    total_sum += i
    total_count += 1
    if i % 2 == 0:
        even_sum += i
        even_count += 1
    else:
        odd_sum += i
        odd_count += 1
```

---

### Level 3 — Pattern Printer + Prime Checker

**Part A — Triangle Pattern:**
```
*
* *
* * *
* * * *
* * * * *
```

```python
# Method A — nested loop (explicit logic)
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Method B — string multiplication (cleaner)
for i in range(1, n+1):
    print("* " * i)
```

**Part B — Prime Finder:**
```
Prime numbers from 2 to 20:
2 3 5 7 11 13 17 19
Total primes found: 8
```

```python
for num in range(2, limit + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        prime_counter += 1
```

---

## 🔑 `range()` Cheat Sheet
```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(5, 0, -1)   # 5, 4, 3, 2, 1
range(1, n+1)     # 1 through n inclusive — most used pattern
```

---

## 🔑 `for...else` — Python's Unique Feature
```python
for i in range(2, num):
    if num % i == 0:
        break           # factor found — not prime
else:
    print("Prime!")     # only runs if NO break occurred
```
> `else` on a for loop = "loop completed without interruption"
> Perfect for: search problems, prime checking, validation

---

## 🔑 Prime Detection — Two Versions

**Readable version — checks all up to num:**
```python
for i in range(2, num):
    if num % i == 0:
        break
```

**Optimized version — checks only up to square root:**
```python
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        break
```

**Why square root works:**
> Every factor pair has one member ≤ √num and one ≥ √num.
> Checking up to √num catches ALL factor pairs.
> For 25: √25=5. Checks 2,3,4,5. Finds 5×5=25. Done.
> Both give correct results. Optimized is faster on large numbers.

**Why `+1`?**
> `range()` excludes stop. Without +1, checking √25=5 stops at 4.
> 25%4≠0 → 25 wrongly marked prime. `+1` includes the square root itself.

---

## 🔑 `end=` Parameter
```python
print("*", end=" ")    # star with space — no newline
print(num, end=" ")    # number inline
print()                # move to next line
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3 