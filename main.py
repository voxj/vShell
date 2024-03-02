logging = False # if you set it to True, then when you run the shell, everything that has the ability to, will log stuff.

__version__ = "1.1"
import os
dir = os.path.dirname(os.path.realpath(__file__))
def lv():
  return logging
def main():
  try:
    from colorama import Fore, Style
    import glob
    from importlib import import_module
  except Exception:
    print('vShell resulted in an error. We\'ll try to fix it.')
    os.system('python -m pip install colorama')
    os.system('pip install colorama')
    from colorama import Fore, Style
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
  print(f'{blue}vShell v{__version__}{reset}')
  while True:
    try:
      x = input(f'{dir}> ').lower()
      if x.startswith('echo '):
          print(x[5:])
      elif x == "help":
        print("Commands")
        print("help - Shows this message")
        print("ver - Shows the version of vShell, but you can put the extension name after ver (aka ver smath) and it'll tell you the version of the module")
        print('offext - Turn off an extension')
        print('onext - Turn on an extension')
        print('To see commands of a specific extension, use help (extension name)')
      elif x == "ver":
        print(f'{blue}vShell {__version__}{reset}')
      elif x.startswith('offext'):
        module_name = x[7:]
        if os.name == "nt":
            os.rename(f'extensions/{module_name}.py', f'extensions/{module_name}.py.dis')
            print(f'The extension won\'t be turned off until you restart the shell.')
        else:
            os.rename(f'extensions/{module_name}.py', f'extensions/{module_name}.py.dis')
            print(f'The extension won\'t be turned off until you restart the shell.')
      elif x.startswith('onext'):
        module_name = x[6:]
        if os.name == "nt":
            os.rename(f'extensions/{module_name}.py.dis', f'extensions/{module_name}.py')
            print(f'The extension won\'t be loaded until you restart the shell.')
        else:
            os.rename(f'extensions/{module_name}.py.dis', f'extensions/{module_name}.py')
            print(f'The extension won\'t be loaded until you restart the shell.')
      elif x == 'exit':
          break
      elif x == '':
          pass
      else:
          command = commands.get(x)
          if command:
              command()
          else:
              print(f'{red}{x} is not a valid command or an application{reset}')
    except Exception as e:
      print(f'{red}An error occured: {e}{reset}')
if __name__ == '__main__':
  main()
else:
  lv()
