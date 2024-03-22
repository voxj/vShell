from tools import retrieve
nt = retrieve.nt()
import os
try:
    from colorama import Fore, Style
except Exception:
    print(f'{__name__} resulted in an error. We\'ll try to fix it.')
    os.system('python -m pip install colorama')
    os.system('pip install colorama')
    os.system('sudo pacman -S python-colorama')
    from colorama import Fore, Style
blue = Fore.BLUE
reset = Style.RESET_ALL
red = Fore.RED
__version__ = "1.3.1"
def ver():
    print(f"{blue}Simply, Math v{__version__} {red}Legacy{reset}")
def helpsmth():
    print("Commands for Simply, Math")
    print("sum - Summary")
    print("sub - Subtraction")
    print("mtp - Multiplication")
    print("div - Division")
    print("exp - Exponentation (or pow - Power)")
    print('xor - XOR')
def initialize():
    if nt == True:
        print(f'Note from {__name__}.py: This extension may have bugs.')
    else:
        pass
def mtp():
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    r = n1 * n2
    if r.is_integer():
        r = int(r)
    print(r)
def sum():
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    r = n1 + n2
    if r.is_integer():
        r = int(r)
    print(r)
def div():
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    r = n1 / n2
    if r.is_integer():
        r = int(r)
    print(r)
def sub():
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    r = n1 - n2
    if r.is_integer():
        r = int(r)
    print(r)
def pow():
    n1 = int(input("First number: "))
    n2 = int(input("Second number: "))
    r = n1 ** n2
    print(r)
def exp():
    r = int(input("First number: ")) ^ int(input("Second number: "))
    print(r)
def register_commands(commands):
    commands['sum -legacy'] = sum
    commands['mtp -legacy'] = mtp
    commands['div -legacy'] = div
    commands['sub -legacy'] = sub
    commands['pow -legacy'] = pow
    commands['exp -legacy'] = pow
    commands['xor -legacy'] = exp
    commands['ver smath -legacy'] = ver
    commands['ver simplymath -legacy'] = ver
    commands['help smath -legacy'] = helpsmth
    commands['help simplymath -legacy'] = helpsmth
