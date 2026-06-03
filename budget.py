"""Budget management and alert system."""
from storage import load_budget, save_budget

def set_budget(amount):
    if amount <= 0:
        raise ValueError("Budget must be greater than 0.")
    budget = load_budget()
    budget['monthly'] = float(amount)
    save_budget(budget)
    return budget['monthly']

def get_budget():
    return load_budget().get('monthly', 0)

def check_budget_alert(total_spent):
    budget = get_budget()
    if budget <= 0:
        return None, 0
    pct = (total_spent / budget) * 100
    if pct >= 100:
        return 'exceeded', pct
    elif pct >= 90:
        return 'critical', pct
    elif pct >= 75:
        return 'warning', pct
    return None, pct
