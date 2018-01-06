# Shorten

Simple tool to shorten any command in your terminal.

## Example

**To shorten a command**:
```
$ shorten echo e
```

Now, try calling that command:
```
$ e "hello, world."

hello, world.
```

Delete a shortened command.
```
$ shorten delete e
```

You can even shorten `shorten`!
```
$ shorten shorten s
```

## How does it work?

When you install `shorten`, it creates a hidden folder in your home directory named `.shorten`. It then adds a line to your `.bash_rc` file that exports this location to your `$PATH` env variable. This directory is where your shortened commands
will be stored.

When you `shorten` a command, it creates a python script in the `~/.shorten` directory that redirects your shortened command to the actual command.

## Install

Clone this repo and pip install:
```
pip install -e .
```
