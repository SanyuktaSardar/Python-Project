# 🔐 PyPassword Generator & Strength Detector

A simple yet powerful **Python CLI tool** to help users **generate secure passwords** and **analyze the strength** of existing ones — all while reinforcing good cybersecurity practices.

---

## 📌 Problem Statement

Weak passwords are a **common cybersecurity vulnerability**. This project addresses that by allowing users to generate **strong, custom passwords** and analyze the strength of their current ones.

---

## 🎯 Project Objective

* ✅ Create a **CLI-based password tool** in Python.
* 🔑 Provide user-controlled password generation.
* 🧠 Analyze password strength and give improvement suggestions.
* 💾 Save valid passwords securely in a file.

---

## 🚀 Features

### 🔐 Password Generator

* User specifies:

  * Number of **uppercase + lowercase letters**
  * Number of **symbols**
  * Number of **numbers**
* Ensures a **minimum password length of 12 characters**
* Characters are randomly shuffled for unpredictability
* Password is saved in a file (`Password.txt`)

### 🔍 Password Strength Detector

* User inputs a password
* Checks for:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
  * Minimum length (12+)
* Feedback:

  * ✅ **Strong**
  * ⚠️ **Medium** (with suggestions)
  * ❌ **Weak**

### 🧯 Error Handling

* Handles:

  * Non-integer inputs
  * Short password constraints
  * File write errors

---

## 🧪 Tech Stack

* **Language:** Python 3.x
* **Libraries:** Built-in (`random`, `input`, `try-except`)
* **Platform:** Command-Line Interface (CLI)

---

## 🗂 Project Structure

```
project/
│
├── password_generator.py             # 🎯 Main Python script
├── Password.txt                      # 💾 Stores generated/verified passwords
├── README.md                         # 📘 Project documentation
│
└── screenshots/                      # 📸 Screenshots for demonstration
    ├── Screenshot 2025-06-24 221404.png   # Generator start prompt
    ├── Screenshot 2025-06-24 221425.png   # User inputs
    ├── Screenshot 2025-06-24 221446.png   # Generated password output
    ├── Screenshot 2025-06-24 221523.png   # Strength detector prompt
    ├── Screenshot 2025-06-24 221615.png   # Medium strength warning
    ├── Screenshot 2025-06-24 222012.png   # Strong password confirmation
    ├── Screenshot 2025-06-24 222032.png   # Prompt to store password
    ├── Screenshot 2025-06-24 222145.png   # Weak password message
    ├── Screenshot 2025-06-24 222203.png   # Password stored feedback
    └── desktop.ini                        # (ignore this system file)
```

---

## 📸 Screenshots

### 🔧 Generator Prompt

![Generator Prompt](https://github.com/SanyuktaSardar/Python-Project/blob/main/project3/Screenshoots/Screenshot%202025-06-24%20221404.png)

### 👤 User Inputs

![User Input](https://github.com/SanyuktaSardar/Python-Project/blob/main/project3/Screenshoots/Screenshot%202025-06-24%20221523.png)

### ✅ Password Generated

![Password Output](https://github.com/SanyuktaSardar/Python-Project/blob/main/project3/Screenshoots/Screenshot%202025-06-24%20222203.png)


### ⚠️ Medium Password Feedback

![Medium Password](https://github.com/SanyuktaSardar/Python-Project/blob/main/project3/Screenshoots/Screenshot%202025-06-24%20222032.png)

### 🎉 Strong Password Message

![Strong Password](https://github.com/SanyuktaSardar/Python-Project/blob/main/project3/Screenshoots/Screenshot%202025-06-24%20222145.png)


---

## 📦 How to Run

1. **Clone the repo:**

   ```bash
   git clone https://github.com/SanyuktaSardar/project3.git
   cd project3
   ```

2. **Run the script:**

   ```bash
   python project3.py
   ```

3. **Choose mode:**

   * Type `c` to create a password
   * Type `d` to detect password strength

---

## 🔐 Security Note

This is an **educational tool**. Passwords are stored in plain text in `Password.txt`. Avoid using real passwords for accounts. Use password managers for actual storage.

---

## 🚀 Future Enhancements

* [ ] GUI using Tkinter or PyQt
* [ ] Clipboard copy feature
* [ ] Password strength score meter
* [ ] Encryption of stored passwords

---

## 👤 Author

**Sanyukta Sardar**
📧 *Contact me for collaborations or suggestions!*
🌐 [GitHub Profile](https://github.com/SanyuktaSardar)

---

