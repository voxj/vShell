######################################
##    VSHELL EXTENSION INSTALLER    ##
######################################
##   PLEASE DON'T DELETE. PLEASE.   ##
######################################

import os
try:
    from colorama import Fore, Style
    import requests
except Exception:
    os.system('python -m pip install colorama')
    os.system('py -m pip install colorama')
    os.system('python -m pip install requests')
    os.system('py -m pip install requests')
    from colorama import Fore, Style
    import requests
import random
from main import dir
Link = 'https://raw.githubusercontent.com/voxj/vShell-ExtInstTest/main/extension.py'
def isNT():
    if os.name == 'nt':
        return True
    else:
        return False
def c():
    if isNT() == True:
        os.system('cls')
    else:
        os.system('clear')
def initialize():
    pass
def vsi():
    global Link
    try:
        c()
        a = input(f'{Fore.BLUE}{dir}{Style.RESET_ALL}> vei install ')
        c()
        b = input(f'{Fore.BLUE}{dir}{Style.RESET_ALL}> vei install {a} ')
        c()
        cd = requests.get(Link.replace('voxj/vShell-ExtInstTest', a)).text
        fps = os.path.join('extensions', f'{b}.py')
        with open(fps, 'w') as afd:
            afd.write(cd)
    except Exception as e:
        print(e)
def vsiurl():
    try:
        c()
        a = input(f'{Fore.BLUE}{dir}{Style.RESET_ALL}> vei install --url ')
        c()
        b = input(f'{Fore.BLUE}{dir}{Style.RESET_ALL}> vei install --url {a} ')
        c()
        cd = requests.get(a).text
        fps = os.path.join('extensions', f'{b}.py')
        with open(fps, 'w') as afd:
            afd.write(cd)
    except Exception as e:
        print(e)
def register_commands(commands):
    commands['vei install '] = vsi
    commands['vei install'] = vsi
    commands['vei install --url'] = vsiurl
    commands['vei install --url '] = vsiurl  
