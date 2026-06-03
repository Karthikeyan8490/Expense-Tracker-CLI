# 💰 Expense Tracker CLI

> **Command-Line Expense Manager — Python · CSV/JSON · Reports · Budget Alerts**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![CLI](https://img.shields.io/badge/Interface-CLI-green.svg)]()
[![Storage](https://img.shields.io/badge/Storage-CSV%20%2F%20JSON-orange.svg)]()

A clean, feature-rich **command-line expense tracker** built in Python. Track daily expenses by category, set monthly budgets, view spending reports, and export your data — all from your terminal.

---

## ✨ Features

- ➕ **Add expenses** with amount, category, description and date
- 📋 **List expenses** — all, by category, or by month
- 📊 **Monthly summary report** with category-wise breakdown
- 🚨 **Budget alerts** — warns when spending exceeds set limit
- 🗑️ **Delete expenses** by ID
- 💾 **Export** to CSV or JSON
- 📁 **Persistent storage** — data saved between sessions
- 🎨 **Colored terminal output** for better readability

---

## 🚀 Quick Start

```bash
git clone https://github.com/Karthikeyan8490/Expense-Tracker-CLI.git
cd Expense-Tracker-CLI

python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac

pip install -r requirements.txt
python main.py
```

---

## 📟 Usage

```bash
# Add an expense
python main.py add --amount 250 --category food --desc "Lunch at cafe"

# List all expenses
python main.py list

# List by category
python main.py list --category food

# Monthly report
python main.py report --month 2025-06

# Set monthly budget
python main.py budget --set 5000

# Delete an expense
python main.py delete --id 3

# Export to CSV
python main.py export --format csv

# Export to JSON
python main.py export --format json
```

---

## 📊 Sample Output

```
============================================
   Expense Tracker - June 2025 Report
============================================
Category       Spent       Budget %
-----------    --------    ----------
Food           ₹2,450      49.0%  ✅
Transport      ₹850        17.0%  ✅
Entertainment  ₹1,200      24.0%  ✅
Others         ₹350        7.0%   ✅
--------------------------------------------
TOTAL          ₹4,850 / ₹5,000
Budget Status: ⚠️ 97% used — Almost at limit!
============================================
```

---

## 📁 Project Structure

```
Expense-Tracker-CLI/
├── main.py              # CLI entry point (argparse)
├── tracker.py           # Core expense logic
├── storage.py           # CSV/JSON read-write
├── reports.py           # Monthly summary & charts
├── budget.py            # Budget management & alerts
├── utils.py             # Colors, formatting helpers
├── data/
│   ├── expenses.json    # Expense records (auto-created)
│   └── budget.json      # Budget settings (auto-created)
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.9+** — Core logic
- **argparse** — CLI interface
- **json / csv** — Data persistence
- **colorama** — Colored terminal output
- **tabulate** — Formatted table output

---

## 👨‍💻 Author

**Bukka Karthikeyan** — MVSR Engineering College, Hyderabad
