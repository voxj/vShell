from main import n
import os
try:
  from colorama import Fore, Style
  pass
except Exception:
  print(f'{__name__} resulted in an error. We\'ll try to fix it.')
  os.system('python -m pip install colorama')
  os.system('pip install colorama')
  os.system('sudo pacman -S python-colorama')
  from colorama import Fore, Style
  pass
blue = Fore.BLUE
reset = Style.RESET_ALL
nt = n()
__version__ = "1.2.1"
def initialize():
  if nt == True:
    print(f'Note from {__name__}.py: This extension doesn\'t have purpose. Disable to save ~0.06ms.')
  else:
    pass
def ver():
  print(f'{blue}OS v{__version__}{reset}')
def oz():
  while True:
    x = input('> ')
    if x == "exit":
      break
    else:
      os.system(x)
def helpos():
  print('Commands for OS')
  print('help os - shows this message')
  print('ver os - shows the version of the extension')
  print('os - opens a shell (doesn\'t work good')
def register_commands(commands):
  commands['os'] = oz
  commands['help os'] = helpos
  commands['ver os'] = ver
