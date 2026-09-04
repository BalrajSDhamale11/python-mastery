# 0.2 — Python Installation and Environment Awareness

## What is PATH?

PATH is an environment variable — a list of file locations stored by the
operating system that tells the terminal where to look for executable
programs when a command name is typed without specifying its full location.

## Checking the environment

- `python --version` → `Python 3.14.6`
- `where python` (CMD) → `E:\All App Files\Python (App Files)\python.exe`,
  because that folder is in CMD's PATH.
- `where python` (VSCode terminal) → nothing appeared.
- `where.exe python` (VSCode terminal) → same path as CMD:
  `E:\All App Files\Python (App Files)\python.exe`.

## Practical lesson

Checked whether VSCode's terminal, CMD, and VSCode's configured interpreter
were all pointing at the same Python install. They were consistent — same
Python, same PATH resolution. This matters because inconsistent PATH across
terminals is a common cause of confusing "works in one terminal, not the
other" bugs (e.g. installing a package in one terminal, then running a script
from a different one that can't find it).