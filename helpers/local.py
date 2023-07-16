import os
import subprocess


def execute_local_command(cmd):
    results = subprocess.run(f"brew {cmd}", shell=True)
    print(f'Command exit: {results.returncode}')