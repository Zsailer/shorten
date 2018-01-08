import os
import stat
import glob
import argparse


def which(program):
    """Check if a command exists.

    Pulled logic from StackOverflow:
    https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python

    Returns None if no program exists.
    """
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def create_alias(command, alias):
    """Create an alias."""
    # Check that command exists
    if which(command) is None:
        raise Exception("The `{}` command doesn't exist.".format(command))

    # Check that alias is ok.
    if which(alias) is not None:
        raise Exception("The `{}` alias is already taken.".format(alias))

    shorten_path = os.path.expanduser('~/.shorten')
    template_path = os.path.join(os.path.split(os.path.realpath(__file__))[0],
                                 'template.py')

    # Check if shorten folder exists. Create if not.
    if not os.path.exists(shorten_path):
        os.makedirs(shorten_path)

    # Read template
    template = "#!/usr/bin/env python \n"
    template += "COMMAND = '{}'\n".format(command)

    with open(template_path, 'r') as f:
        template += f.read()

    # alias path
    alias_path = os.path.join(shorten_path, alias)

    # Write template file
    with open(alias_path, 'w') as f:
        f.write(template)

    # Check file to executable
    st = os.stat(alias_path)
    os.chmod(alias_path, st.st_mode | stat.S_IEXEC)


def delete_alias(alias):
    """Delete an alias from the database."""
    # Find shorten database location
    shorten_path = os.path.expanduser('~/.shorten')
    alias_path = os.path.join(shorten_path, alias)

    # Remove tree.
    os.remove(alias_path)


def list_aliases():
    """Print list of aliases in terminal."""
    # Get all aliases files in shorten database.
    shorten_path = os.path.expanduser('~/.shorten')
    fnames = glob.glob(os.path.join(shorten_path, "*"))

    # Print header
    print('Alias\t\tCommand')
    print('-----\t\t-------')

    # Print aliases and command.
    for fn in fnames:
        alias = os.path.split(fn)[1]
        with open(fn, 'r') as f:
            c = f.readlines()[1].strip()
            command = c[c.find("'")+1:-1]
            print("{}\t\t{}".format(alias, command))
