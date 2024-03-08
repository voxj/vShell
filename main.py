__version__ = "1.7"
import os
from tools import retrieve
def cont():
  pass
dir = os.path.dirname(os.path.realpath(__file__))
def main():
  try:
    from colorama import Fore, Style
    import json
    import glob
    import requests
    from importlib import import_module
  except Exception:
    print('vShell resulted in an error. We\'ll try to fix it.')
    os.system('python -m pip install colorama')
    os.system('sudo pacman -S python-colorama')
    os.system('pip install colorama')
    os.system('python -m pip install requests')
    os.system('pip install requests')
    os.system('sudo pacman -S python-requests')
    from colorama import Fore, Style
    import requests
    import glob
    from importlib import import_module
  reset = Style.RESET_ALL
  red = Fore.RED
  false = False
  true = True
  green = Fore.GREEN
  blue = Fore.BLUE
  extensions_dir = 'extensions'
  extension_files = glob.glob(f'{extensions_dir}/*.py')
  commands = {}
  def init():
    with open('settings.json', 'r') as stgs:
      data = json.load(stgs)
      if retrieve.st() == "release" or retrieve.st() == "Release":
        pass
      else:
        if retrieve.fr() == true:
          print(f'{red}vShell v{__version__} is currently in {retrieve.st()} state. Use only at your risk.{reset}')
        elif retrieve.sa() == true:
          print(f'{red}vShell v{__version__} is currently in {retrieve.st()} state. Use only at your risk.{reset}')
        else:
          pass
      devMode = data['devMode']
      logging = devMode
      enableNotes = data['Notes']
      betaExts = data['betaExts']
      if logging == True:
        print('Loading extensions')
      elif logging == False:
        pass
      for extension_file in extension_files:
          module_name = os.path.basename(extension_file)[:-3]
          if module_name.startswith('beta-'):
            if betaExts == True:
              pass
            else:
              os.rename(f'extensions/{module_name}.py', f'extensions/{module_name}.py.beta-dis')
              print(f'A beta extension {module_name} was turned off, since you haven\'t enabled betaExts. You have to turn on betaExts and manually change the name of the extension from .py.beta-dis to .py.')
              print('The program is gonna shutdown to prevent further crashes.')
              exit()
          try:
            module = import_module(f'{extensions_dir}.{module_name}')
            if hasattr(module, 'initialize'):
                module.initialize()
            if hasattr(module, 'register_commands'):
                module.register_commands(commands)
            if logging == True:
              print(f'{module_name}: {green}SUCCESS{reset}')
            elif logging == False:
              pass
          except Exception as e:
            print(f'The extension {module_name} had an error. Not initializing.')
            ad = input('Would you like to see the error cause? ')
            if ad.lower() == "y":
              print(e)
  init()
  if commands == {}:
    print('No extensions loaded. Are you running the script from the correct folder?')
  else:
    pass
  with open('settings.json','r') as a:
    data = json.load(a)
  def about():
    print(f'About {blue}vShell{reset}')
    print('This app starts off something like "bare bones" and gets better with extensisons.')
  if retrieve.st() == "release" or retrieve.st() == "Release":
    print(f'{blue}vShell v{__version__}{reset}')
  else:
    print(f'{blue}vShell v{__version__} {red}{retrieve.st()}{reset}')
  while True:
    try:
      with open('settings.json', 'r') as stgs:
        data = json.load(stgs)
      if data['echo'] == True:
        x = input(f'{blue}{dir}{reset}> ')
      else:
        x = input()
      if x == "echo on":
        data['echo'] = True
      elif x == "echo off":
        data['echo'] = False
      elif x.startswith('echo '):
        print(x[5:])
      elif x == "echo":
        pass
      elif x == "help" or x == "help 1":
        print("Commands • Page 1")
        print("help - Shows this message")
        print("ver/ver [extension-name]- Shows the version of vShell, but you can put the extension name after ver (aka ver smath) and it'll tell you the version of the module")
        print('offext [extension] - Turn off an extension')
        print('onext [extension] - Turn on an extension')
        print('echo [text] - Echo\'s your text')
        print('echo on/off - Turns on/off the location> input')
        print('about - Tells about this app')
        print('suggest [text] - Make a suggestion for further updates')
        if retrieve.dm():
          print('cmddump - Used for debug, dumps all existing shell commands and their actual Python functions')
        print('Page 1 out of 2. Use help 2 to see page 2.')
        print('To see commands of a specific extension, use help (extension name)')
      elif x == "help 2":
        print("Commands • Page 2")
        print('help 2 - Shows this message')
        print("devMode on/off - Turns developer mode on/off")
        print("betaExts on/off - Turns beta extensions on/off, currently doesn't do anything")
        print("notes on/off - Turns the startup notes on/off")
        print("reload - Reloads the shell")
        if retrieve.st().lower() != "release":
          print("alertonstart on/off - Turns on the alert on start on/off (it only runs for the first run if you haven't turned it on)")
        print('Page 2 out of 2. Use help to see page 1.')
        print('To see commands of a specific extension, use help (extension name)')
      elif x == "ver":
        print(f'{blue}vShell {__version__}{reset}')
      elif x.startswith('alertonstart '):
        s = x[13:]
        if s == "on":
          data['NonStopAlertRadio'] = True
          print(f'Operation {green}succesful{reset}')
        elif s == "off":
          data['NonStopAlertRadio'] = false
          print(f'Operation {green}succesful{reset}')
        else:
          print(f'{red}{s} is not a valid argument for alertonstart{reset}')
      elif x.startswith("betaExts "):
        s = x[9:]
        if s == "on":
          data['betaExts'] = true
          print(f'Operation {green}succesful{reset}')
        elif s == "off":
          data['betaExts'] = false
          print(f'Operation {green}succesful{reset}')
        else:
          print(f'{red}{s} is not a valid argument for betaExts{reset}')
      elif x == "reload":
        main()
      elif x.startswith('devMode '):
        s = x[8:]
        if s == "on":
          data['betaExts'] = True
          print(f'Operation {green}succesful{reset}')
        elif s == "off":
          data['betaExts'] = false
          print(f'Operation {green}succesful{reset}')
        else:
          print(f'{red}{s} is not a valid argument for betaExts{reset}')
      elif x == "cmddump":
        print(commands)
      elif x == "notes on":
        data['Notes'] = true
      elif x == "notes off":
        data['Notes'] = false
      elif x.startswith('offext'):
        module_name = x[7:]
        os.rename(f'extensions/{module_name}.py', f'extensions/{module_name}.py.dis')
        print('The extension won\'t be turned off until you restart the shell.')
      elif x.startswith('onext'):
        module_name = x[6:]
        os.rename(f'extensions/{module_name}.py.dis', f'extensions/{module_name}.py')
        print('The extension won\'t be loaded until you restart the shell.')
      elif x.startswith('suggest'):
        content = x[8:]
        headers = {'Content-Type': 'application/json',}
        user = os.getlogin()
        ting = {'content': f'Suggestion by {user}: {content}',}
        response = requests.post('https://discord.com/api/webhooks/1213909155405111426/DD-H4YICy1SGgHB_Ram5LgZ6XlvM49tx4MKfIiL9goGcF89os5FlD63gm0uDrBOq4fBR', headers=headers, data=json.dumps(data))
        print('Suggestion sent! Thanks :3')
      elif x == 'about':
        about()
      elif x == 'exit':
        with open('settings.json', 'w') as stgs:
          data['firstRun'] = false
          json.dump(data, stgs)
        break
      elif x == '':
          pass
      else:
          command = commands.get(x)
          if command:
              command()
          else:
              print(f'{red}{x} is not a valid command or an application, run help to see commands{reset}')
      with open('settings.json', 'w') as stgs:
        data['firstRun'] = false
        json.dump(data, stgs)
    except Exception as e:
      print(f'{red}An error occured: {e}{reset}')
    except KeyboardInterrupt:
      print('\nTo exit, run exit or close the terminal')
      pass
if __name__ == '__main__':
  main()
else:
  pass
