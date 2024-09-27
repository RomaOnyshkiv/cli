#!venv/bin/python
from cmnds import remote
from cmnds import local
from cmnds import generate_pass
from cmnds.ip_helper import IpCalculator
from serv.services import Services

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
@click.option("--ips", help="ip addresses in format: \"0.0.0.0/x, 1.1.1.1/x, ...\"")
def calculate_ip_range(ips):
    all_ips = ips.split(",")
    total_amount_of_ips = 0
    if len(all_ips) > 0:
        for addr in range(len(all_ips)):
            iprange = IpCalculator(all_ips[addr]).get_ip_range()
            n_add = f'| Network address        | {iprange["network_address"]}'
            b_add = f'| Broadcast address      | {iprange["broadcast_address"]}'
            f_add = f'| First usable IP        | {iprange["first_usable_ip"]}'
            l_add = f'| Last usable IP         | {iprange["last_usable_ip"]}'
            t_add = f'| Total usable addresses | {iprange["total_usable_hosts"]}'
            ip, net_mask = all_ips[addr].split("/")
            total_amount_of_ips = total_amount_of_ips + iprange["total_usable_hosts"]
            print(f'\nResults for IP Range {addr +1} -> {ip.strip()}\nwith subnet -> {net_mask}:')
            print(f'=' * table_width + s.sp(n_add) + s.sp(b_add) + s.sp(f_add) + s.sp(l_add) + s.sp(t_add))
    total = f'| Total usable hosts     | {total_amount_of_ips}'
    print(f'\n\nRanges: {all_ips}')
    print(f'=' * table_width + s.sp(total))


@click.command(name="iptobin", help="convert IP tp binary")
@click.option("--ips", help="type IP addresses")
def to_bin(ips):
    all_ips = ips.split(',')
    for ip in all_ips:
        ip_bin = IpCalculator(ip).ip_to_bin()
        rez = f'| IP {ip.strip()}' + ' ' * (19 - (4 + len(ip.strip()))) + f'| {ip_bin.strip()} '
        print(f'Address: {ip.strip()} of {all_ips}\n' + f'=' * table_width + s.sp(rez))


cli.add_command(execute_on_remote2)
cli.add_command(generate_password)
cli.add_command(run_local)
cli.add_command(run_brew)
cli.add_command(execute_on_remote)
cli.add_command(calculate_ip_range)
cli.add_command(to_bin)

if __name__ == '__main__':
    table_width = 60
    s = Services(table_width=table_width)
    cli()
