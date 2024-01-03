#!/usr/bin/env python3
from mylib.calc import *

import click


@click.group()
def cli():
    """A calculator program"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cmd(a, b):
    """Add two numbers

    Example:
    ./calCLI.py add 1 2
    """
    click.secho(f"{a} + {b} = {add(a,b)}", fg="green")


if __name__ == "__main__":
    cli()
