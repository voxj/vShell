import os
from tools import retrieve
import sys
pyver = sys.version
__version__ = "1.1"
devMode = retrieve.dm()
try:
    import colorama
except Exception:
  print(f'{__name__} resulted in an error. We\'ll try to fix it.')
  os.system('python -m pip install colorama')
  os.system('pip install colorama')
  os.system('sudo pacman -S python-colorama')
  try:
    import colorama
  except Exception:
    print(f'Automatic error fixing for {__name__} hasn\'t worked. Please disable the extension or download a previous version of it.')
blue = colorama.Fore.BLUE
reset = colorama.Style.RESET_ALL
def initialize():
  if devMode == True:
    print(f'{blue}superPY v{__version__} with Python {pyver}{reset}')
  else:
    pass
def open_shell():
    os.system('python')
def verpy():
    print(f'{blue}superPY v{__version__} | Wanted to see the shell version? Use ver pyshell!')
def pyshve():
    print(f'{blue}Python {pyver}{reset} | Wanted to see the extension version? Use ver spy!')
def helppy():
    print('Commands for Python')
    print('help py (or help python) - shows this message')
    print('ver py (or ver python) - tells the version of the extension')
    print('superPY - opens a Python shell')
def register_commands(commands):
    commands['superPY'] = open_shell
    commands['help spy'] = helppy
    commands['help superPY'] = helppy
    commands['ver spy'] = verpy
    commands['ver superPY'] = verpy
    commands['ver pyshell'] = pyshve
