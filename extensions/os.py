from main import lv
import os
try:
  from colorama import Fore, Style
  pass
except Exception:
  os.system('python -m pip install colorama')
  os.system('pip install colorama')
  from colorama import Fore, Style
  pass
blue = Fore.BLUE
reset = Style.RESET_ALL
log = lv()
__version__ = "1.1"
def initialize():
  if log == True:
    print(f'Note from {__name__}.py: The OS extension is not too good yet, but if you really insist on using it, well.. okay I guess...')
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
def register_commands(commands):
  commands['os'] = oz
  commands['ver os'] = ver
