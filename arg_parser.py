import json
import sys

# get the current working directory, commands, values and flags
cwd = sys.argv[0]
cmds = sys.argv[1].split(':')
vals = [arg for arg in sys.argv[2::] if not arg.startswith('-' or '--')]
flags = [arg for arg in sys.argv[2::] if arg.startswith('-' or '--')]

# open the commands json file
with open('commands.json') as commands_json:
  commands_json = json.load(commands_json)
  
# use the commands to find the specific action
data = commands_json
for cmd in cmds:
  data = data[cmd]

# DEV: print the action selected
print(data)
