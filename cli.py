#!venv/bin/python
from cmnds import remote
from cmnds import local
from cmnds import generate_pass

import click


@click.group()
def cli():
    pass


@click.command(name="br", help="Run brew command")
@click.option("--cm", default="update", help="Brew command to be executed")
def run_brew(cm):
    local.execute_brew_command(cm)


@click.command(name="local", help="Run command on local")
@click.option("--cm", default="ls -lah", help="Run command on local")
def run_local(cm):
    local.execute_local_command(cm)


@click.command(name="remote", help="Run command on remote")
@click.option("--cm", default="ls -lah", help="Command to be executed on remote")
@click.option("--server", help="Remote host name")
@click.option("--usr", help="Remote user")
@click.option("--pswd", help="Remote password. Can be configured as environment variable 'export REMOTE_PASS=...'")
def execute_on_remote(cm, server, usr, pswd):
    remote.run_ssh_command(cm, server, usr, pswd)


@click.command(name="password", help="Generate password")
@click.option("--total", type=int, help="The total password length. If passed, it will ignore -n, -l, -u and -s, and generate completely random passwords with the specified length")
@click.option("--numbers", default=0, help="Number of digits in the PW", type=int)
@click.option("--lower", default=0, help="Number of lowercase chars in the PW", type=int)
@click.option("--upper", default=0, help="Number of uppercase chars in the PW", type=int)
@click.option("--spec", default=0, help="Number of special chars in the PW", type=int)
@click.option("--amount", default=1, type=int, help="Amount")
@click.option("--output")
def generate_password(total, numbers, lower, upper, spec, amount, output):
    generate_pass.generate(total, numbers, lower, upper, spec, amount, output)


@click.command(name="remote2", help="Run command on remote server")
@click.option("--host", help="Remote Hostname")
@click.option("--pwd", help="Remote password")
@click.option("--usr", help="Remote username")
@click.option("--command", help="Command to be executed")
@click.option("--file", help="script file")
def execute_on_remote2(host, pwd, usr, command, file):
    remote.run_on_remote(host, pwd, usr, command, file)


cli.add_command(execute_on_remote2)
cli.add_command(generate_password)
cli.add_command(run_local)
cli.add_command(run_brew)
cli.add_command(execute_on_remote)

if __name__ == '__main__':
    cli()
