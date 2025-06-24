---

# 🔐 PyPassword Generator & Strength Detector

## 📌 Project Overview

### The PyPassword Generator is a Command-Line Interface (CLI) tool built in Python that allows users to:

# ✅ Generate strong, custom passwords with letters, numbers, and symbols.
# 🔍 Detect password strength based on character types and length.
# 💾 Optionally save passwords** securely in a local text file.

This tool helps promote better password practices and reinforces programming fundamentals such as conditionals, loops, exception handling, and file operations.

---

## 🎯 Features

### 🔑 Password Generator

* User can define:

  * Number of **letters** (upper + lower)
  * Number of **symbols**
  * Number of **digits**
* Enforces a **minimum length** of 12 characters.
* Randomly distributes characters and shuffles them.
* Saves the generated password to `Password.txt`.

### 🔍 Password Strength Detector

* Evaluates user-provided passwords.
* Checks for:

  * ✅ Uppercase letters
  * ✅ Lowercase letters
  * ✅ Digits
  * ✅ Symbols
  * ✅ Minimum 12 characters
* Gives feedback:

  * 🎉 **Strong**
  * 😐 **Medium** (with suggestions)
  * ❌ **Weak**

### 🧯 Exception Handling

* Handles invalid or negative input.
* Handles file write errors.

---

## 💻 How to Use

1. **Run the program:**

```bash
python password_generator.py
```

2. **Choose a mode:**

   * Type `c` → to create a new password.
   * Type `d` → to detect strength of an existing password.

3. **Follow on-screen prompts.**

---

## 📂 File Structure

project/
│
├── password_generator.py           # 🎯 Main Python script
├── Password.txt                    # 💾 Stores generated or verified passwords
├── README.md                       # 📘 Project documentation
│
└── screenshots/                    # 📸 Demo screenshots folder
    ├── Screenshot 2025-06-24 221404.png   # Generator start prompt
    ├── Screenshot 2025-06-24 221425.png   # User input for password
    ├── Screenshot 2025-06-24 221446.png   # Generated password output
    ├── Screenshot 2025-06-24 221523.png   # Strength detection prompt
    ├── Screenshot 2025-06-24 221615.png   # Medium strength feedback
    ├── Screenshot 2025-06-24 222012.png   # Strong password detection
    ├── Screenshot 2025-06-24 222032.png   # User prompt to save password
    ├── Screenshot 2025-06-24 222145.png   # Weak password warning
    ├── Screenshot 2025-06-24 222203.png   # Save confirmation / end screen
    └── desktop.ini                        # (Auto-generated system file, can be ignored)

```

---

## 🔧 Tech Stack

* **Language:** Python 3.x
* **Modules:** `random` (built-in)

---

## 📌 Example Outputs

### ➕ Password Generation

```
Welcome to the PyPassword Generator!
Type 'c' to create a password or 'd' to detect password strength: c
How many letters would you like in your password? 6
How many symbols would you like? 3
How many numbers would you like? 3
✅ Your generated password is: A9$fB3&c7!
💾 Password saved to Password.txt
```

### 🔎 Password Strength Detection

```
Enter your password: abc123
⚠️ Medium Password: Your password length is 6. Please add 6 more characters.
```

---

## 🚀 Future Enhancements

* [ ] Add clipboard copy functionality with `pyperclip`
* [ ] Add password strength score
* [ ] Convert to GUI using `Tkinter`
* [ ] Encrypt stored passwords

---

## 🔐 Security Note

> This tool is for educational use. Passwords are stored in **plain text**. Do **not** use real passwords for sensitive accounts.

---

## 👩‍💻 Author

Developed by **Sanyukta Sardar** as part of a Python project portfolio.
Feel free to fork, star, and contribute!

---
