def ver():
  print(f"{blue}vHook v1.0{reset}")

while True:
  try:
    import os
    import json
    import requests
    from colorama import Fore, Style
    red = Fore.RED
    reset = Style.RESET_ALL
    blue = Fore.BLUE
    from main import lv
    log = lv()
    break
  except Exception:
    print('vHook resulted in an error. We\'ll try to fix it.')
    import os
    os.system('py -m pip install requests')
    os.system('pip install requests')
    os.system('py -m pip install colorama')
    os.system('pip install colorama')
    import requests
    import json
    from colorama import Fore, Style
    red = Fore.RED
    reset = Style.RESET_ALL
    blue = Fore.BLUE
    from main import lv
    log = lv()
    break
def helpvhk():
  print('Commands for vHook')
  print('send - Sends a message using a webhook')
def initialize():
  if log == True:
    print(f'{blue}vHook v1.0{reset}')
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
      if log == True:
          print(f'Done: {response.status_code}')
      else:
        if response.status_code == 204:
          print('Done!')
        else:
          print(f'{red}An error occured: {response.text}{reset}')
    except Exception as e:
      print(f'{red}An error occured: {e}{reset}')
      pass
def version():
  print('')
def register_commands(commands):
  commands['send'] = sendds
  commands['ver vhook'] = ver