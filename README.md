# Shorten

Simple (Python) tool to shorten any command in your terminal.

`shorten` takes the place of adding aliases in your bash profile. It also makes a few things a more convenient. For example, you can
  1. create an alias from any location,
  2. list your aliases and
  3. search aliases by leading characters.

## Things you can do

**Create an alias.** Call `shorten` (from anywhere!) on any command and give it an alias.

```
$ shorten echo e
Alias successfully added.
```
```
$ # Let's try it out!
$ echo 'Hello, world!'
Hello, world!
```

**Remove an alias.** Call `shorten delete`.
```
$ shorten delete e
```

**List all your aliases.**
```
$ shorten list all

Alias         Command
-----         -------
ipynb         jupyter notebook
jlab          jupyter lab
e             echo
```

**List aliases that start with substring.**
```
$ shorten list ip

Alias         Command
-----         -------
ipynb         jupyter notebook
```

**Protip**: shorten `shorten` ;).
```
$ shorten shorten s
```

## How does it work?

*Shorten* creates a hidden folder in your home directory. This is where your aliases will be stored. Each alias is actually a python script that redirects the alias to the true command.

*Shorten* adds a line to your bash profile that points your $PATH variable to `~/.shorten`. If you can't get your aliases to work (or you're using another shell like Zsh), check that the following line is in the right `rc` file.

```
export PATH="~/.shorten:$PATH"
```


## Install

Clone this repo and pip install:
```
pip install -e .
```
