import os
from tools import retrieve
import sys
pyver = sys.version
__version__ = "1.1.1"
devMode = retrieve.dm()
try:
    import colorama
except Exception:
  print(f'{__name__} has an error. Autofixes aren\'t applied due to their unstability.')
blue = colorama.Fore.BLUE
reset = colorama.Style.RESET_ALL
def initialize():
  if devMode == True:
    print(f'{blue}superPY v{__version__} with Python {pyver}{reset}')
  else:
    pass
def open_shell():
    os.system('py')
def verpy():
    print(f'{blue}superPY v{__version__} | Wanted to see the shell version? Use ver pyshell!{reset}')
def pyshve():
    print(f'{blue}Python {pyver} | Wanted to see the extension version? Use ver spy!{reset}')
def helppy():
    print('Commands for Python')
    print('help py (or help python) - shows this message')
    print('ver py (or ver python) - tells the version of the extension')
    print('spy - opens a Python shell')
def register_commands(commands):
    commands['spy'] = open_shell
    commands['help spy'] = helppy
    commands['help superPY'] = helppy
    commands['ver spy'] = verpy
    commands['ver superPY'] = verpy
    commands['ver pyshell'] = pyshve
