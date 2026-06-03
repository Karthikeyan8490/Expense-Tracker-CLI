"""Monthly report generation."""
from tracker import get_monthly_totals
from budget  import get_budget, check_budget_alert
from utils   import green, red, yellow, cyan, bold, fmt_currency, fmt_bar
from datetime import datetime

def print_monthly_report(month=None):
    if not month:
        month = datetime.today().strftime('%Y-%m')
    totals, grand_total = get_monthly_totals(month)
    budget   = get_budget()
    alert, pct = check_budget_alert(grand_total)

    print(bold(f"\n{'='*48}"))
    print(bold(f"  Expense Report - {month}"))
    print(bold(f"{'='*48}"))
    print(f"  {'Category':<16} {'Spent':>10}   {'Share':>8}")
    print(f"  {'-'*42}")

    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        if amt > 0:
            share = (amt / grand_total * 100) if grand_total else 0
            line  = f"  {cat.capitalize():<16} {fmt_currency(amt):>10}   {share:>6.1f}%"
            print(green(line) if share < 30 else yellow(line))

    print(f"  {'-'*42}")
    total_line = f"  {'TOTAL':<16} {fmt_currency(grand_total):>10}"
    if budget > 0:
        total_line += f"  / {fmt_currency(budget)}"
    print(bold(total_line))

    if budget > 0:
        bar_color = green if alert is None else (yellow if alert == 'warning' else red)
        print(f"\n  Budget:  {bar_color(fmt_bar(min(pct,100)))}")
        if alert == 'exceeded':
            print(red("  BUDGET EXCEEDED! Please review your expenses."))
        elif alert == 'critical':
            print(red(f"  WARNING: {pct:.1f}% of budget used!"))
        elif alert == 'warning':
            print(yellow(f"  NOTICE: {pct:.1f}% of budget used."))
        else:
            print(green(f"  Budget usage: {pct:.1f}% - You're on track!"))

    print(bold(f"{'='*48}\n"))
