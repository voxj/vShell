__version__ = "1.3.4"
from tools import retrieve
devMode = retrieve.dm()
def ver():
  print(f"{blue}vHook {__version__}{reset}")

while True:
  try:
    import os
    import json
    import requests
    from colorama import Fore, Style
    break
  except Exception:
    print(f'{__name__} has an error. Autofixes aren\'t applied due to their unstability.')
    break
red = Fore.RED
reset = Style.RESET_ALL
blue = Fore.BLUE
def helpvhk():
  print('Commands for vHook')
  print('send - Sends a message using a webhook')
  print('ver vhook - shows the version of the extension')
  print('help vhook - shows this message')
def initialize():
  if devMode == True:
    print(f'{blue}vHook v{__version__}{reset}')
  else:
    pass
def sendds():
  wbu = input('Webhook URL: ')
  msg = input('Message: ')
  send_discord_message(url=wbu,content=msg)
def send_discord_message(url, content):
    headers = {'Content-Type': 'application/json',}
    data = {'content': content,}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
      if devMode == True:
          print(f'Done: {response.status_code}')
      else:
        if response.status_code == 204:
          print('Done!')
        else:
          print(f'{red}An error occured: {response.text}{reset}')
    except Exception as e:
      print(f'{red}An error occured: {e}{reset}')
      pass
def register_commands(commands):
  commands['send'] = sendds
  commands['ver vhook'] = ver
  commands['help vhook'] = helpvhk
