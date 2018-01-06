

# Is the COMMAND variable defined above?
__doc__ = "Template for creating an alias."

import sys
import subprocess

if __name__ == "__main__":

    # Arguments without the alias
    args = sys.argv[1:]

    command = [COMMAND]
    command += args

    subprocess.call(command)
