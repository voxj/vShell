from main import lv
import os
try:
  from colorama import Fore, Style
except Exception:
  print(f'{__name__} resulted in an error. We\'ll try to fix it.')
  os.system('python -m pip install colorama')
  os.system('pip install colorama')
  from colorama import Fore, Style
blue = Fore.BLUE
reset = Style.RESET_ALL
log = lv()
__version__ = "1.2"
def ver():
  print(f"{blue}Simple Math v{__version__}{reset}")
def helpsmth():
  print("Commands for Simple Math")
  print("sum - Summary")
  print("sub - Subtraction")
  print("mtp - Multiplication")
  print("div - Division")
def initialize():
  if log == True:
    print(f'Note from {__name__}.py: The Simple Math extension may have bugs.')
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
def register_commands(commands):
  commands['sum'] = sum
  commands['mtp'] = mtp
  commands['div'] = div
  commands['sub'] = sub
  commands['ver smath'] = ver
  commands['ver simplemath'] = ver
  commands['help smath'] = helpsmth
  commands['help simplemath'] = helpsmth
