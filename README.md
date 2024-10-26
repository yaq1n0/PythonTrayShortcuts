# PythonTrayShortcuts
 Create your own custom tray launchpad with python scripts

## Setup (user)
- install python 3.13 or later
- `pip install -r requirements.txt`
- `python3 main.py`
- you can then add the above command to launch on boot etc. 

## Testing
- test suffix "_test"
- `unittest` python builtin testing library

## TODO: 
- proper testing integration with visual studio code
- auto format code on save in vs code
- code completions/intellsense in vs code

- load UI configuration from json file {"items", ["key1", "SEPERATOR", "key2"]}
- subprocess execution (execute .py file from runner) and drag n drop scripts into `/scripts`

- launch on boot support (Windows, MacOS, Linux?). Potentially can make this work as an intrinsic script that does OS detection and executes commands
- custom logo.png support (should be possible, default to defaultLogo.png in hidden folder)

- support for launch with admin rights (Windows), elevated (sudo) permissions in Linux and potentially bypassing some MacOS limitations (might need to deal with some stupid Apple Mac API shit)

- determine async behavior, do we FIFO? 




