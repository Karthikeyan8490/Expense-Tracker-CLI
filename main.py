"""
Expense Tracker CLI - Entry Point
Usage: python main.py <command> [options]
"""
import argparse, sys
from tracker import add_expense, list_expenses, delete_expense
from reports import print_monthly_report
from budget  import set_budget, get_budget
from storage import export_csv, export_json
from utils   import green, red, yellow, cyan, bold, fmt_currency
from tabulate import tabulate

def cmd_add(args):
    try:
        exp = add_expense(args.amount, args.category, args.desc or '', args.date)
        print(green(f"\n  Added: {exp['category'].capitalize()} — "
                    f"{fmt_currency(exp['amount'])} on {exp['date']}  [ID: {exp['id']}]"))
    except ValueError as e:
        print(red(f"\n  Error: {e}"))
        sys.exit(1)

def cmd_list(args):
    expenses = list_expenses(
        category=args.category,
        month=args.month
    )
    if not expenses:
        print(yellow("\n  No expenses found."))
        return
    rows = [[e['id'], fmt_currency(e['amount']),
             e['category'].capitalize(), e['description'], e['date']]
            for e in expenses]
    total = sum(e['amount'] for e in expenses)
    print(bold(f"\n  Expenses ({len(expenses)} records)"))
    print(tabulate(rows, headers=['ID','Amount','Category','Description','Date'],
                   tablefmt='rounded_outline'))
    print(bold(f"\n  Total: {fmt_currency(total)}"))

def cmd_delete(args):
    try:
        delete_expense(args.id)
        print(green(f"\n  Deleted expense ID {args.id}."))
    except ValueError as e:
        print(red(f"\n  Error: {e}"))

def cmd_report(args):
    print_monthly_report(args.month)

def cmd_budget(args):
    if args.set:
        amt = set_budget(args.set)
        print(green(f"\n  Monthly budget set to {fmt_currency(amt)}"))
    else:
        b = get_budget()
        if b:
            print(cyan(f"\n  Current monthly budget: {fmt_currency(b)}"))
        else:
            print(yellow("\n  No budget set. Use: python main.py budget --set <amount>"))

def cmd_export(args):
    expenses = list_expenses()
    if not expenses:
        print(yellow("\n  No expenses to export."))
        return
    if args.format == 'csv':
        f = export_csv(expenses)
    else:
        f = export_json(expenses)
    print(green(f"\n  Exported {len(expenses)} records to {f}"))

def main():
    print(bold(cyan("\n  💰 Expense Tracker CLI")))
    parser = argparse.ArgumentParser(
        prog='expense-tracker',
        description='Track your expenses from the command line.'
    )
    sub = parser.add_subparsers(dest='command', required=True)

    # add
    p_add = sub.add_parser('add', help='Add a new expense')
    p_add.add_argument('--amount',   type=float, required=True, help='Expense amount')
    p_add.add_argument('--category', required=True,
                       choices=['food','transport','entertainment','health',
                                'shopping','utilities','education','others'])
    p_add.add_argument('--desc',   default='', help='Description')
    p_add.add_argument('--date',   default=None, help='Date (YYYY-MM-DD)')

    # list
    p_list = sub.add_parser('list', help='List expenses')
    p_list.add_argument('--category', default=None)
    p_list.add_argument('--month',    default=None, help='YYYY-MM')

    # delete
    p_del = sub.add_parser('delete', help='Delete an expense by ID')
    p_del.add_argument('--id', type=int, required=True)

    # report
    p_rep = sub.add_parser('report', help='Monthly summary report')
    p_rep.add_argument('--month', default=None, help='YYYY-MM')

    # budget
    p_bud = sub.add_parser('budget', help='Set or view monthly budget')
    p_bud.add_argument('--set', type=float, default=None)

    # export
    p_exp = sub.add_parser('export', help='Export expenses to file')
    p_exp.add_argument('--format', choices=['csv','json'], default='csv')

    args = parser.parse_args()
    cmds = {
        'add': cmd_add, 'list': cmd_list, 'delete': cmd_delete,
        'report': cmd_report, 'budget': cmd_budget, 'export': cmd_export,
    }
    cmds[args.command](args)

if __name__ == '__main__':
    main()
