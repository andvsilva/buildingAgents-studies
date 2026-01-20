# Python Developer Roadmap

> From fundamentals to professional workflows — a structured learning path

---

## 1. Python Basics

### 1.1 What is Python

* High-level, interpreted, dynamically typed language
* Emphasis on readability and simplicity
* Used in web, data, AI, automation, science

### 1.2 First Program

```python
print("Hello, world!")
```

### 1.3 Variables and Data Types

* `int`, `float`, `str`, `bool`

```python
age = 30
name = "Andre"
height = 1.75
is_active = True
```

### 1.4 Operators

* Arithmetic: `+ - * / // % **`

### 1.5 Input and Output

```python
age = int(input("Enter your age: "))
print(age + 1)
```

---

## 2. Control Flow

### 2.1 Conditional Statements

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### 2.2 Loops

#### 2.2.1 for loop

```python
for i in range(5):
    print(i)
```

#### 2.2.2 while loop

```python
count = 0
while count < 3:
    count += 1
```

#### 2.2.3 Loop Control

* `break`
* `continue`

---

## 3. Functions

### 3.1 Defining Functions

```python
def add(a, b):
    return a + b
```

### 3.2 Default Arguments

```python
def greet(name="Guest"):
    print(name)
```

### 3.3 Multiple Return Values

```python
def calc(a, b):
    return a+b, a-b
```

---

## 4. Modules

### 4.1 Creating Modules

* One `.py` file = one module

### 4.2 Importing Modules

```python
import math
from math import sqrt
import math as m
```

### 4.3 `__main__` Guard

```python
if __name__ == "__main__":
    main()
```

---

## 5. Error Handling & Debugging

### 5.1 Types of Errors

* Syntax Errors
* Runtime Errors (Exceptions)
* Logical Errors

### 5.2 try / except

```python
try:
    x = int(input())
except ValueError:
    print("Invalid input")
```

### 5.3 else and finally

### 5.4 Raising Exceptions

```python
raise ValueError("Invalid value")
```

### 5.5 Debugging Tools

* `print`
* `assert`
* `pdb`
* Tracebacks

### 5.6 Logging

```python
import logging
logging.info("message")
```

---

## 6. Unit Testing

### 6.1 What are Unit Tests

* Test small units of code
* Prevent regressions

### 6.2 unittest

```python
import unittest
```

### 6.3 pytest

```python
assert add(2, 3) == 5
```

### 6.4 Testing Exceptions

### 6.5 Fixtures and Edge Cases

---

## 7. Virtual Environments & Package Management

### 7.1 Virtual Environments

```bash
python -m venv .venv
```

### 7.2 Activation

```bash
source .venv/bin/activate
```

### 7.3 pip Basics

```bash
pip install requests
```

### 7.4 requirements.txt

```bash
pip freeze > requirements.txt
```

---

## 8. Git Basics

### 8.1 Repository Initialization

```bash
git init
```

### 8.2 Commit Workflow

```bash
git add .
git commit -m "message"
```

### 8.3 Push and Pull

```bash
git push
git pull
```

### 8.4 Branches

```bash
git switch -c feature-x
```

---

## 9. GitHub Collaboration

### 9.1 Feature Branch Workflow

* Branch → PR → Review → Merge

### 9.2 Fork & Pull Model

### 9.3 Pull Requests

* Small
* Focused
* CI passing

### 9.4 Code Reviews

### 9.5 Rebase vs Merge

---

## 10. CI/CD

### 10.1 Continuous Integration

* Automated tests on push

### 10.2 GitHub Actions Example

```yaml
on: [push]
```

### 10.3 Protected Branches

---

## 11. Clean, Readable, Modular Python Code

### 11.1 Readability & Naming

### 11.2 Single Responsibility Principle

### 11.3 Modularity & Project Structure

### 11.4 Type Hints

```python
def average(values: list[float]) -> float:
    return sum(values)/len(values)
```

### 11.5 Docstrings

### 11.6 DRY Principle

### 11.7 PEP 8 & Formatting

* black
* ruff

---

## 12. Next Powerful Topics

### 12.1 Object-Oriented Programming

* Classes and objects
* Encapsulation
* Inheritance
* Composition

### 12.2 SOLID Principles

* Single Responsibility
* Open/Closed
* Liskov Substitution
* Interface Segregation
* Dependency Inversion

### 12.3 Design Patterns

* Factory
* Strategy
* Adapter
* Observer

### 12.4 Advanced Testing

* Mocking
* Coverage
* Property-based testing

### 12.5 Async Programming

```python
async def fetch():
    await asyncio.sleep(1)
```

### 12.6 Performance & Profiling

### 12.7 Packaging & Distribution

### 12.8 Application Architecture

### 12.9 Security Basics

### 12.10 Deployment & DevOps

---

## 13. Recommended Learning Path

```
Python Basics
→ Testing
→ Git & CI
→ Clean Code
→ OOP & SOLID
→ Design Patterns
→ Architecture & Async
```

---

## 14. Final Note

This roadmap represents a **professional Python developer foundation**, suitable for backend, data, automation, and AI-oriented careers.

Happy coding 🐍🚀
