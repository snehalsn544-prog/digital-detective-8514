# Mission 4 — Programming

**Goal:** write and run a small Python program, recognize basic programming building blocks, and compare interpreted and compiled execution.

## 1. What is a program?

A program is a set of instructions that a computer follows. Python source files usually end in `.py`. An editor is where you write the code; the Python interpreter is the program that executes it.

## 2. Check Python on macOS

Open Terminal and run:

```bash
python3 --version
```

If a version is displayed, Python 3 is available. If the command is not found, install Python 3 from [python.org](https://www.python.org/downloads/).

## 3. Create and run a Python file

From the repository folder, create `hello.py` inside this mission folder using your editor. Put this code in it:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print("Hello,", name)
print("Next year you will be", age + 1)
```

Run it from the repository root:

```bash
python3 mission-04-programming/hello.py
```

Example interaction (your own input will differ):

```text
What is your name? Asha
How old are you? 18
Hello, Asha
Next year you will be 19
```

**Understand the code:**
- `name` and `age` are variables: names that refer to values.
- `input()` reads text typed by the user.
- `int()` converts numeric text to an integer.
- `print()` displays output.
- The expression `age + 1` performs arithmetic.

## 4. Conditions and loops

Try this separate example:

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

for count in range(1, 4):
    print("Practice", count)
```

The `if/else` selects a path. The `for` loop repeats its indented block three times. Change the input and predict the output before running it.

## 5. Interpreter and compiler

| Interpreter (typical description) | Compiler (typical description) |
|---|---|
| Runs a program through a runtime that processes instructions or bytecode | Translates source code into another form, often native machine code, before execution |
| Often supports quick edit-and-run development | Often produces a separate executable or build output |
| Errors can appear while the program runs | Many syntax/type errors can be reported during compilation |

**Important nuance:** Python is commonly called an interpreted language, but standard CPython first compiles source code to bytecode and then its virtual machine executes that bytecode. So “interpreted versus compiled” is a useful beginner comparison, not an absolute division.

A compiled-language example (optional, if a C compiler is installed) is:

```bash
clang --version
```

You do not need to install a compiler just to finish the Python exercise.

## 6. Your experiment log

Complete this table after running the examples yourself.

| Experiment | What I changed | What happened |
|---|---|---|
| Name and age program |  |  |
| Even/odd program |  |  |
| Loop range |  |  |

## 7. Check your understanding

1. What is the difference between source code and program output?
2. Why is `int(input(...))` used when reading an age?
3. What does the `if` statement decide?
4. How many times does `range(1, 4)` repeat the loop?
5. Why is it not fully accurate to say that Python does no compilation?

## Reflection

- One program I successfully ran:
- One error I encountered and how I fixed it:
- In my own words, an interpreter:
- In my own words, a compiler:

## Completion checklist

- [ ] Checked that Python 3 runs on my computer.
- [ ] Created and ran the name-and-age program.
- [ ] Tested the condition and loop example.
- [ ] Completed the experiment log and reflection.
- [ ] Added only genuine, privacy-safe evidence if required.

**Submission note:** The examples and explanations are provided as a guide. Run the programs yourself and write your own observations; do not claim an experiment was performed until you have done it.
