#!venv/bin/python
import click


@click.group()
def cli():
    pass


@click.command(name="upd")
def update():
    click.echo(f'Update command is in development')


cli.add_command(update)

if __name__ == '__main__':
    cli()
