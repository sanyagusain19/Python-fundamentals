# Python Fundamentals

A concise beginner reference covering core Python concepts up through functions. Each section lists what to learn and a short example or exercise to practice.

## Topics covered

1. Variables & basic types  
   - What to cover: integers, floats, booleans, None, basic type conversion, and truthiness.  
   - Example/exercise: convert user input to int/float safely; write expressions that test truthiness (e.g., empty vs non-empty values).

2. Basic operators & expressions  
   - What to cover: arithmetic (+, -, *, /, //, %), comparison (==, !=, <, >, <=, >=), logical (and, or, not), membership (in, not in), and assignment operators (+=, *=). Operator precedence and short-circuit behavior.  
   - Example/exercise: evaluate mixed expressions showing precedence; swap two variables without a temporary variable.

3. Strings  
   - What to cover: creation, indexing, slicing, immutability, common methods (split, join, replace, strip, lower/upper), and f-strings for formatting.  
   - Example/exercise: parse "2026-06-19" into year/month/day integers and format back as "June 19, 2026" using an f-string.

4. Collections: lists, tuples, sets, dicts (intro)  
   - What to cover: differences (mutable vs immutable), basic creation and access, common operations and methods for each (append/pop for lists, indexing for tuples, set uniqueness/operations, dict get/set and iteration). When to choose each.  
   - Example/exercise: given a list with duplicates, produce a list of unique items preserving original order; count frequencies into a dict.

5. Control flow  
   - What to cover: if / elif / else, for loops, while loops, break and continue, and loop-else semantics. Best practices for readable conditionals.  
   - Example/exercise: iterate a list of numbers and find the first prime using a loop with break; demonstrate an else branch that runs when no prime is found.

6. Functions  
   - What to cover: define with def, return values, positional and keyword arguments, default arguments, *args and **kwargs, docstrings, and basic annotations. Purity (side effects) vs. impure functions.  
   - Example/exercise: write a function `mean(values, *, ignore_none=True)` that returns the average of numeric items and documents its behavior in a docstring.

## How to use this guide
- Study the topics in order; implement the short exercises after reading each section.  
- Keep examples small and test them in the jupyter nb or a single script file.  
- Focus on understanding behaviors (mutability, scope, evaluation order) rather than memorizing APIs.

---
Created with ❤️ by @sanyagusain19
