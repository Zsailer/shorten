

# Is the COMMAND variable defined above?
__doc__ = "Template for creating an alias."

import os
import sys
import subprocess

if __name__ == "__main__":

    # Arguments without the alias
    args = sys.argv[1:]

    command = COMMAND.split(' ')
    command += args

    # Handling annoying ~ in subprocess.
    for i, c in enumerate(command):
        if '~' in c:
            command[i] = os.path.expanduser(c)

    # Handle chdir. This is a hack. Keeps a python subprocess
    # to change directory.
    if command[0] in ['cd', 'chdir']:
        os.chdir("".join(command[1:]))
        os.system(os.environ['SHELL'])
    else:
        subprocess.call(command)
