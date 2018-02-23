# -*- coding: utf-8 -*-

"""Console script for hello_world_flask."""

import click


@click.command()
def main(args=None):
    """Console script for hello_world_flask."""
    click.echo("Replace this message by putting your code into "
               "hello_world_flask.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
