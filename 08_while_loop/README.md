# 🔁 Concept 08: While Loop

> **Core Idea:** Run a block of code repeatedly as long as a condition is True.
> While loops are for when you don't know how many times to repeat.
> "Keep going until something happens" — that's a while loop.

---

## 🧠 Key Concepts Covered
- While loop structure — initializer, condition, updater
- `break` — exit loop immediately
- `continue` — skip current iteration, go back to condition
- `while True` + `break` pattern — standard input validation
- Infinite loops — what they are and how to avoid them
- Attempt counters — counting only valid iterations

---

## 💡 Golden Rules
- Every while loop needs 3 things: **initializer, condition, updater**
- Missing updater = infinite loop. `Ctrl + C` to escape.
- `while True` runs forever — `break` is the ONLY exit
- Put `input()` inside the loop ONCE — never duplicate it
- Only increment counters for valid inputs — placement matters
- `continue` skips print/logic — loop condition still checked next
- While loop = unknown iterations. For loop = known iterations.

---

## 📝 Problems Solved

### Level 1 — The Countdown Timer
Count down from user's number to 1, then print Blastoff.

**Key skill:** Basic while loop. Decrementing counter. Post-loop print.

```
Enter starting number: 5
5
4
3
2
1
🚀 Blastoff!
```

```python
starting_number = int(input("Enter starting number: "))

while starting_number >= 1:
    print(starting_number)
    starting_number -= 1

print("🚀 Blastoff!")
```

---

### Level 2 — The Input Validator
Keep asking for a number between 1-10 until valid input received.

**Key skill:** `while True` + `break` pattern. Eliminating input duplication.

```
Enter a number between 1 and 10: 15
❌ Invalid! Please enter between 1 and 10.
Enter a number between 1 and 10: 7
✅ Valid input received: 7
```

**Standard input validation pattern:**
```python
while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        break
    print("❌ Invalid! Please enter between 1 and 10.")

print(f"✅ Valid input received: {number}")
```

> `input()` appears exactly ONCE — no duplication.
> `break` fires only when input is valid.
> This is the pattern used in real codebases.

---

### Level 3 — The Number Guessing Game
Full interactive game — secret number, higher/lower hints, attempt counter, performance rating.

**Key skill:** Nested logic inside while loop. Valid-only attempt counting. Post-loop rating.

```
Enter your guess: 10
📉 Too low! Try higher.

Enter your guess: 15
📈 Too high! Try lower.

Enter your guess: 13
🎉 Correct! You got it in 3 attempts!
⭐⭐⭐ Excellent Guesser!
```

```python
secret_number = 13
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    if 1 <= guess <= 20:
        attempts += 1          # only valid guesses counted
        if guess == secret_number:
            print(f"🎉 Correct! You got it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try higher.")
        else:
            print("📈 Too high! Try lower.")
    else:
        print("Enter a valid number!")

if attempts <= 3:
    print("⭐⭐⭐ Excellent Guesser!")
elif attempts <= 6:
    print("⭐⭐ Good Guesser!")
else:
    print("⭐ Keep Practicing!")
```

---

## 🔑 The Three Loop Elements
```python
count = 1             # 1. INITIALIZER — where to start
while count <= 5:     # 2. CONDITION   — when to keep going
    print(count)
    count += 1        # 3. UPDATER     — move toward ending
```

---

## 🔑 break vs continue
```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue    # skips print for 3 — goes back to condition
    if count == 5:
        break       # exits loop entirely — 5 never prints
    print(count)
# Output: 1 2 4
```

---

## 🔑 Known Gap — To Fix Later
```python
# If user enters "abc" — program crashes with ValueError
# Fix: Exception Handling (covered in later concept)
guess = int(input("Enter guess: "))  # crashes on non-numeric input
```

---

## ✅ Status: Mastered
**Hints used:** 0 | **Levels cleared:** 3/3