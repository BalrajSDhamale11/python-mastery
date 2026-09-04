# 0.3 — Basic Debugging Workflow

## Reading a traceback

Read from the bottom up — the most recent/deepest event (where the actual error occurred) is printed at the very bottom, not the top. The last line gives the exception type and message; the lines above show the call chain that led there.

## Example: NameError from a typo

`NameError: name 'pricess' is not defined`

Root cause: a typo — `pricess` instead of `prices`. Not a SyntaxError (code structure was valid, so the parser had no problem with it); the error only surfaced once Python actually tried to look up a name that didn't exist.

## Practical takeaway

When a `NameError` shows a name that closely resembles another name used nearby, scan for a near-identical name — that's almost always a typo, not a deeper logic error. A `NameError` on a name that doesn't resemble anything nearby is more likely a real bug (never defined, wrong scope).