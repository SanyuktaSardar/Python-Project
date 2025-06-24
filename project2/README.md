# 📊 Monthly Expenses Manager 🧾

A Python-based **command-line utility** to help users **track**, **analyze**, and **visualize** their monthly expenses. Built using **pandas** for data handling and **matplotlib** for visualization, this tool supports budgeting, spending insights, and CSV-based tracking.

---

## 🚀 Features

* ✅ Add expenses with **category**, **description**, **quantity**, **price**, and **date**
* 📝 Edit or remove existing entries using their index
* 📅 Filter data by **month**, **year**, or **category**
* 📃 Display entries in a clean tabular format
* 💰 View total expenses for any given month
* 📊 Visualize spending with:

  * 🥧 **Pie chart** (category-wise for a selected month)
  * 📉 **Bar chart** (category-wise or month-wise)
* 📁 Stores all records in a persistent local file (`Monthly Expenses.csv`)

---

## 📁 Project Structure

```
Monthly-Expenses-Manager/
│
├── expenses_manager.py               # 🎯 Main Python script
├── Monthly Expenses.csv              # 📄 CSV file created automatically
├── README.md                         # 📘 Project documentation
└── screenshots/                      # 📸 Output visualizations and app interface
    ├── Screenshot 2025-06-24 171410.png
    ├── Screenshot 2025-06-24 171542.png
    ├── Screenshot 2025-06-24 171819.png
    ├── Screenshot 2025-06-24 171908.png
    ├── Screenshot 2025-06-24 171943.png
    ├── Screenshot 2025-06-24 172016.png
    ├── Screenshot 2025-06-24 172036.png
    ├── Screenshot 2025-06-24 172124.png
    ├── Screenshot 2025-06-24 172151.png
    ├── Screenshot 2025-06-24 172212.png
    ├── Screenshot 2025-06-24 172241.png
    ├── Screenshot 2025-06-24 172255.png
    └── desktop.ini                      # (system-generated, ignored)
```

---

## 🛠 Requirements

* Python 3.x
* Install dependencies:

```bash
pip install pandas matplotlib
```

---

## ▶️ How to Run

```bash
python project2.py
```

Choose from the menu:

* Add Expense
* Edit/Delete Entry
* Show Records
* Generate Pie/Bar Chart
* Show Total for a Month
* Exit

---

## 🖼️ Screenshots

### ➕ Add Expense

![Add Expense](https://github.com/SanyuktaSardar/Python-Project/blob/main/project2/screenshoot/Screenshot%202025-06-24%20171542.png)


### 📊 Pie Chart

![Pie Chart](https://github.com/SanyuktaSardar/Python-Project/blob/main/project2/screenshoot/Screenshot%202025-06-24%20172036.png)

### 📉 Bar Chart

![Bar Chart](https://github.com/SanyuktaSardar/Python-Project/blob/main/project2/screenshoot/Screenshot%202025-06-24%20172124.png)

### 📈 Expense Summary

![Summary](https://github.com/SanyuktaSardar/Python-Project/blob/main/project2/screenshoot/Screenshot%202025-06-24%20172241.png)

---

## 💡 Use Cases

* Personal or family budgeting
* Student or freelancer expense tracking
* Daily/weekly/monthly finance management
* Expense visualization for reports or journals

---

## 📌 Future Enhancements

* GUI using Tkinter or PyQt
* Export summaries as PDF/Excel
* Smart category suggestions
* Login system for multi-user access

---

## 👩‍💻 Author

**Sanyukta Sardar**
*Crafted with Python, DataFrames & Charts.* 🐍📊

