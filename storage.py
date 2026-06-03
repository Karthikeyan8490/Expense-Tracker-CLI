"""Handles reading and writing expense data to JSON and CSV."""
import json, csv, os
from datetime import datetime

DATA_DIR     = os.path.join(os.path.dirname(__file__), 'data')
EXPENSE_FILE = os.path.join(DATA_DIR, 'expenses.json')
BUDGET_FILE  = os.path.join(DATA_DIR, 'budget.json')

def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_expenses():
    _ensure_data_dir()
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    _ensure_data_dir()
    with open(EXPENSE_FILE, 'w') as f:
        json.dump(expenses, f, indent=2, default=str)

def load_budget():
    _ensure_data_dir()
    if not os.path.exists(BUDGET_FILE):
        return {"monthly": 0}
    with open(BUDGET_FILE, 'r') as f:
        return json.load(f)

def save_budget(budget):
    _ensure_data_dir()
    with open(BUDGET_FILE, 'w') as f:
        json.dump(budget, f, indent=2)

def export_csv(expenses, filename='expenses_export.csv'):
    if not expenses:
        return None
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id','amount','category','description','date'])
        writer.writeheader()
        writer.writerows(expenses)
    return filename

def export_json(expenses, filename='expenses_export.json'):
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent=2, default=str)
    return filename
