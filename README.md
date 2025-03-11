# Errors Library

## What is this?
This module defines a collection of absurdly specific and completely unnecessary errors!
Perfect for blaming the user, the author, the code, your machine, or even the laws of logic itself.


Use at your own risk... please, for the love of God!


## Why does this exist?

Because... sometimes standard exceptions like `ValueError` or `RuntimeError` just don’t cut it. Sometimes, you need to express just how screwed up shit is with more *precision*.
And how dumb your users are.

## Installation
`pip install errorslib`

## Usage
Raise these errors when you need to make a point, confuse a junior developer, or just vent your frustration in a productive way;

```python
from absurd_errors import *

# Blame the user
raise UserIsAnIdiotError("PEBKAC")

# Blame the developer
raise ForgotToImplementError("one job")

# Blame the code
raise CodeIsFuckedUpError("you found out my code SUCKS")

# Blame reality
raise ParadoxError("This should not be happening...")
```

## Error Categories

- **User Errors** – Because sometimes the problem *is* between the keyboard and the chair.
- **Developer Errors** – When the author is the real problem.
- **Code Errors** – If your spaghetti code finally collapses.
- **Hardware Errors** – The computer *swears* it’s not its fault.
- **Logic Errors** – When logic decides to take a vacation.
- **Miscellaneous WTF Errors** – For when you truly have no idea what’s happening.

## Notable Errors

| Error Name                      | When to Use |
|---------------------------------|------------------------------------------------|
| `UserIsAnIdiotError`           | When the user clearly did something dumb. |
| `FeatureNotABugError`          | When it’s a "feature" (totally not a bug). |
| `OopsIDidItAgainError`         | When you make the same mistake… again. |
| `WTFNoOS`                      | When the OS is mysteriously *gone*. |
| `WTFNoBIOS`                    | 🎶 How did this happen 🎶 |
| `ThisErrorShouldNeverHappenError` | When an "impossible" bug occurs. |
| `ParadoxError`                 | When reality collapses. |

## License
MIT License. Use at your own risk, and don't sue me if you actually put this into production and get fired.
