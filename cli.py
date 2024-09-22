#!venv/bin/python
from cmnds import remote
from cmnds import local
from cmnds import generate_pass
from cmnds import personal_helper as helper

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
@click.option("--total", type=int,
              help="The total password length. If passed, it will ignore -n, -l, -u and -s, and generate completely random passwords with the specified length")
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


@click.command(name="netrange", help="Calculate range of IPs")
@click.option("--ip", help="ip address in format: 0.0.0.0/x")
def calculate_ip_range(ip):
    iprange = helper.get_ip_range(ip)
    n_add = f'| Network address        | {iprange["network_address"]}'
    b_add = f'| Broadcast address      | {iprange["broadcast_address"]}'
    f_add = f'| First usable IP        | {iprange["first_usable_ip"]}'
    l_add = f'| Last usable IP         | {iprange["last_usable_ip"]}'
    t_add = f'| Total usable addresses | {iprange["total_usable_hosts"]}'
    ip, net_mask = ip.split("/")
    print(f'Results for IP -> {ip} with subnet -> {net_mask}:')
    print(f'=' * l + sp(n_add) + sp(b_add) + sp(f_add) + sp(l_add) + sp(t_add))


def sp(space_holder):
    return "\n" + space_holder + " " * (l - len(space_holder) - 1) + "|\n" + '=' * l


cli.add_command(execute_on_remote2)
cli.add_command(generate_password)
cli.add_command(run_local)
cli.add_command(run_brew)
cli.add_command(execute_on_remote)
cli.add_command(calculate_ip_range)

if __name__ == '__main__':
    l = 80
    cli()
