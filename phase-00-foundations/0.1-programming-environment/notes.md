# 0.1 — Python and the Programming Environment

## What is Python?

Python is an interpreted language. The source code we write is interpreted
by the Python interpreter line by line, without needing us to convert it into
machine code ourselves. That step is handled automatically, where source
code is converted into bytecode and then the PVM executes that bytecode.

## Two ways to use the Python interpreter

### 1. REPL
Stands for Read, Evaluate, Print, Loop. We type `python`/`python3` in the
terminal and an interactive prompt appears (`>>>`). Each line we type is
read, evaluated, and its result printed immediately, then the loop continues
for the next line. Best use: learning the basics or quickly experimenting
with code.

### 2. Script Execution
We save Python code in a `script.py` file and run it:

1. The `python` command invokes the Python interpreter executable installed
   on our machine.
2. The interpreter locates and opens `script.py`.
3. It reads the source code and internally compiles it into bytecode. This
   happens automatically, without us needing to compile manually (unlike compiled
   languages like C/C++).
4. The Python Virtual Machine (PVM) executes the bytecode line by line.
5. Output gets printed to the terminal as it runs.
6. If an unhandled error occurs, a traceback is printed and the program
   terminates immediately. Execution cannot pause and resume; the script
   must be fixed and re-run from the start.