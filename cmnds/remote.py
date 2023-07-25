import os
import subprocess


def run_ssh_command(cmd, server, usr, pswd):
    password = os.environ["REMOTE_PASS"] if (pswd is None) else pswd
    results = subprocess.run(("sshpass", "-p", password, "ssh", f'{usr}@{server}', cmd))
    print(f'Exit code: {results.returncode}')


def get_remote_session(pswd):
    password = os.environ["REMOTE_PASS"] if (pswd is None) else pswd
