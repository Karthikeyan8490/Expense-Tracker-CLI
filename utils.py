"""Terminal color helpers and formatting utilities."""
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False
    class Fore:
        RED=GREEN=YELLOW=CYAN=WHITE=BLUE=MAGENTA=''
    class Style:
        BRIGHT=RESET_ALL=''

def green(t):   return f"{Fore.GREEN}{Style.BRIGHT}{t}{Style.RESET_ALL}" if COLOR else t
def red(t):     return f"{Fore.RED}{Style.BRIGHT}{t}{Style.RESET_ALL}"   if COLOR else t
def yellow(t):  return f"{Fore.YELLOW}{t}{Style.RESET_ALL}"              if COLOR else t
def cyan(t):    return f"{Fore.CYAN}{t}{Style.RESET_ALL}"                if COLOR else t
def bold(t):    return f"{Style.BRIGHT}{t}{Style.RESET_ALL}"             if COLOR else t

def fmt_currency(amount):
    return f"Rs.{amount:,.2f}"

def fmt_bar(pct, width=20):
    filled = int((pct / 100) * width)
    bar    = '#' * filled + '-' * (width - filled)
    return f"[{bar}] {pct:.1f}%"
