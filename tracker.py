"""Core expense tracking logic."""
from datetime import datetime
from storage import load_expenses, save_expenses

CATEGORIES = ['food', 'transport', 'entertainment', 'health',
              'shopping', 'utilities', 'education', 'others']

def add_expense(amount, category, description, date=None):
    expenses = load_expenses()
    category = category.lower()
    if category not in CATEGORIES:
        raise ValueError(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    new_id = max((e['id'] for e in expenses), default=0) + 1
    expense = {
        'id':          new_id,
        'amount':      float(amount),
        'category':    category,
        'description': description,
        'date':        date or datetime.today().strftime('%Y-%m-%d'),
    }
    expenses.append(expense)
    save_expenses(expenses)
    return expense

def list_expenses(category=None, month=None):
    expenses = load_expenses()
    if category:
        expenses = [e for e in expenses if e['category'] == category.lower()]
    if month:
        expenses = [e for e in expenses if e['date'].startswith(month)]
    return expenses

def delete_expense(expense_id):
    expenses = load_expenses()
    original = len(expenses)
    expenses = [e for e in expenses if e['id'] != expense_id]
    if len(expenses) == original:
        raise ValueError(f"Expense ID {expense_id} not found.")
    save_expenses(expenses)
    return True

def get_monthly_totals(month=None):
    if not month:
        month = datetime.today().strftime('%Y-%m')
    expenses = list_expenses(month=month)
    totals = {cat: 0.0 for cat in CATEGORIES}
    for e in expenses:
        totals[e['category']] += e['amount']
    return totals, sum(totals.values())
