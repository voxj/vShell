from tools import retrieve, acls
from main import dir
nt = retrieve.nt()
def cls():
  acls.cls()
import os
try:
  from colorama import Fore, Style
except Exception:
  print(f'{__name__} has an error. Autofixes aren\'t applied due to their unstability.')
blue = Fore.BLUE
reset = Style.RESET_ALL
__version__ = "1.4.1"
def ver():
  print(f"{blue}Simply, Math v{__version__}{reset}")
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
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> mtp '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> mtp {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> mtp {n1} {n2}')
  cls()
  r = n1 * n2
  if r.is_integer():
    r = int(r)
  print(f'{blue}{dir}{reset}> mtp {n1} {n2}\n{blue}{reset}{r}')
def sum():
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> sum '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> sum {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> sum {n1} {n2}')
  cls()
  r = n1 + n2
  if r.is_integer():
    r = int(r)
  print(f'{blue}{dir}{reset}> sum {n1} {n2}\n{blue}{reset}{r}')
def div():
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> div '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> div {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> div {n1} {n2}')
  cls()
  r = n1 / n2
  if r.is_integer():
    r = int(r)
  print(f'{blue}{dir}{reset}> div {n1} {n2}\n{blue}{reset}{r}')
def sub():
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> sub '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> sub {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> sub {n1} {n2}')
  cls()
  r = n1 ^ n2
  print(f'{blue}{dir}{reset}> sub {n1} {n2}\n{blue}{reset}{r}')
def pow():
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> pow '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> pow {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> pow {n1} {n2}')
  cls()
  r = n1 ** n2
  print(f'{blue}{dir}{reset}> pow {n1} {n2}\n{blue}{reset}{r}')
def exp2():
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> exp '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> exp {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> exp {n1} {n2}')
  cls()
  r = n1 ** n2
  print(f'{blue}{dir}{reset}> exp {n1} {n2}\n{blue}{reset}{r}')
def exp():
  cls()
  n1 = int(input(f'{blue}{dir}{reset}> xor '))
  cls()
  n2 = int(input(f'{blue}{dir}{reset}> xor {n1} '))
  cls()
  print(f'{blue}{dir}{reset}> xor {n1} {n2}')
  cls()
  r = n1 ^ n2
  print(f'{blue}{dir}{reset}> xor {n1} {n2}\n{r}{reset}')
def register_commands(commands):
  commands['sum'] = sum
  commands['mtp'] = mtp
  commands['div'] = div
  commands['sub'] = sub
  commands['pow'] = pow
  commands['exp'] = exp2
  commands['xor'] = exp
  commands['ver smath'] = ver
  commands['ver simplymath'] = ver
  commands['help smath'] = helpsmth
  commands['help simplymath'] = helpsmth
