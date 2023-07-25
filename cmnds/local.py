import os
import subprocess


def execute_brew_command(cmd):
    results = subprocess.run(f"brew {cmd}", shell=True)
    print(f'Command exit: {results.returncode}')


def execute_local_command(cmd):
    results = subprocess.run(f'{cmd}', shell=True)
    print(f'Exit code: {results.returncode}')