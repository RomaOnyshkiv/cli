#!venv/bin/python
from helpers import remote
from helpers import local

import click


@click.group()
def cli():
    pass


@click.command(name="br", help="Run brew command")
@click.option("--cm", default="update", help="Command to be executed on local machine")
def update(cm):
    local.execute_local_command(cm)


@click.command(name="remote")
@click.option("--cm", default="ls -lah", help="Command to be executed on remote")
@click.option("--server", default='roman', help="Remote host name")
@click.option("--usr", default="root", help="Remote user")
@click.option("--pswd", help="Remote password. Can be configured as environment variable 'export REMOTE_PASS=...'")
def execute_on_remote(cm, server, usr, pswd):
    remote.run_ssh_command(cm, server, usr, pswd)


cli.add_command(update)
cli.add_command(execute_on_remote)

if __name__ == '__main__':
    cli()
