on = True
off = False

devMode = on # in v1.0/v1.1 it was called logger
betaExts = on # new thing, use it to get the beta extensions

logging = devMode
__version__ = "1.3"
import os
dir = os.path.dirname(os.path.realpath(__file__))
def lv():
  return logging
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
    os.system('pacman -S python-colorama')
    os.system('pip install colorama')
    os.system('python -m pip install requests')
    os.system('pip install requests')
    os.system('pacman -S python-requests')
    from colorama import Fore, Style
    import requests
    import glob
    from importlib import import_module
  reset = Style.RESET_ALL
  red = Fore.RED
  green = Fore.GREEN
  blue = Fore.BLUE
  extensions_dir = 'extensions'
  extension_files = glob.glob(f'{extensions_dir}/*.py')
  commands = {}
  def init():
      if logging == True:
        print('Loading extensions')
      elif logging == False:
        pass
      for extension_file in extension_files:
          module_name = os.path.basename(extension_file)[:-3]
          if module_name.startswith('beta-'):
            if betaExts == on:
              pass
            else:
              os.rename(f'extensions/{module_name}.py', f'extensions/{module_name}.py.beta-dis')
              print(f'A beta extension {module_name} was turned off, since you haven\'t enabled betaExts. You have to turn on betaExts and manually change the name of the extension from .py.beta-dis to .py.')
              print('The program is gonna shutdown to prevent further crashes.')
              exit()
          module = import_module(f'{extensions_dir}.{module_name}')
          if hasattr(module, 'initialize'):
              module.initialize()
          if hasattr(module, 'register_commands'):
              module.register_commands(commands)
          if logging == True:
            print(f'Loaded {module_name}')
          elif logging == False:
            pass
  init()
  def about():
    print(f'About {blue}vShell v{__version__}{reset}')
    print('This app starts off something like "bare bones" and gets better with extensisons.')
    print('At first, I made it just for a little test, but then I got into "HYPER CODING MODE" and started updating some stuff in this app at HYPER CODING SPEED.')
  print(f'{blue}vShell v{__version__}{reset}')
  while True:
    try:
      x = input(f'{blue}{dir}{reset}> ').lower()
      if x.startswith('echo '):
          print(x[5:])
      elif x == "help":
        print("Commands")
        print("help - Shows this message")
        print("ver - Shows the version of vShell, but you can put the extension name after ver (aka ver smath) and it'll tell you the version of the module")
        print('offext - Turn off an extension')
        print('onext - Turn on an extension')
        print('about - Tells about this app')
        print('suggestion - Make a suggestion for further updates')
        print('To see commands of a specific extension, use help (extension name)')
      elif x == "ver":
        print(f'{blue}vShell {__version__}{reset}')
      elif x.startswith('offext'):
        module_name = x[7:]
        os.rename(f'extensions/{module_name}.py', f'extensions/{module_name}.py.dis')
        print('The extension won\'t be turned off until you restart the shell.')
      elif x.startswith('onext'):
        module_name = x[6:]
        os.rename(f'extensions/{module_name}.py.dis', f'extensions/{module_name}.py')
        print('The extension won\'t be loaded until you restart the shell.')
      elif x.startswith('suggestion'):
        content = x[11:]
        headers = {'Content-Type': 'application/json',}
        data = {'content': content,}
        response = requests.post('https://discord.com/api/webhooks/1213909155405111426/DD-H4YICy1SGgHB_Ram5LgZ6XlvM49tx4MKfIiL9goGcF89os5FlD63gm0uDrBOq4fBR', headers=headers, data=json.dumps(data))
      elif x == 'about':
        about()
      elif x == 'exit':
          break
      elif x == '':
          pass
      else:
          command = commands.get(x)
          if command:
              command()
          else:
              print(f'{red}{x} is not a valid command or an application, run help to see commands{reset}')
    except Exception as e:
      print(f'{red}An error occured: {e}{reset}')
    except KeyboardInterrupt:
      print('\n')
      print('To exit, run exit or close the terminal')
      pass
if __name__ == '__main__':
  main()
else:
  lv()
