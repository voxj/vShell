import time
import os
import random
from main import dir
from tools import acls
def cls():
    acls.cls()
try:
    import colorama
except Exception:
  print(f'{__name__} has an error. Autofixes aren\'t applied due to their unstability.')
Fore = colorama.Fore
Style = colorama.Style
blue = Fore.BLUE
reset = Style.RESET_ALL
__version__ = '1.3.1'
def initialize():
    pass
def prgb():
    t = random.randint(1, 5)
    try:
        cls()
        x = float(input(f'{blue}{dir}{reset}> pgb '))
        if x <= 0:
            x = 1
        p = x / 100
        for i in range(101):
            if t == 1:
                print('Windows 11 Pro 24H2')
            elif t == 2:
                print('Windows 10 Pro 1903')
            elif t == 3:
                print('Windows Vista Ultimate')
            elif t == 4:
                print('iPhone 20 Leaks')
            elif t == 5:
                print('vShell v2.2 Secret Sneak Peek')
            progress = i // 2
            print(f'{i}% |{"#" * progress}{"-" * (50 - progress)}| 100%')
            time.sleep(p)
            cls()
    except ValueError:
        print("Invalid input.")
def vp():
    print(f'{blue}Progress Bar {__version__}{reset}')
def hp():
    print('Commands for Progress Bar')
    print('progressbar/prgb/progress/pgb - Opens a progress bar (download)')
    print('ver pgb/progressbar - Tells the version of Progress Bar')
    print('help pgb/progressbar - Shows this message')
def register_commands(commands):
    commands['progressbar'] = prgb
    commands['prgb'] = prgb
    commands['progress'] = prgb
    commands['pgb'] = prgb
    commands['ver pgb'] = vp
    commands['ver prgb'] = vp
    commands['ver progressbar'] = vp
    commands['help pgb'] = hp
    commands['help progressbar'] = hp
    commands['help prgb'] = hp
