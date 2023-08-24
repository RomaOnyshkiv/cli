import os
import subprocess
import paramiko


def run_ssh_command(cmd, server, usr, pswd):
    password = os.environ["REMOTE_PASS"] if (pswd is None) else pswd
    results = subprocess.run(("sshpass", "-p", password, "ssh", f'{usr}@{server}', cmd))
    print(f'Exit code: {results.returncode}')


def get_remote_session(pswd):
    password = os.environ["REMOTE_PASS"] if (pswd is None) else pswd


def run_on_remote(host, pwd, usr, command, file):
    pswd = os.environ["REMOTE_PASS"] if (pwd is None) else pwd
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=usr, password=pswd)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    if file:
        execute_me = open(file).read()
    else:
        if command:
            execute_me = command
        else:
            print("No file or command")
            exit()

    stdin, stdout, stderr = client.exec_command(execute_me)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

    client.close()
    print("=" * 10 + " done " + "=" * 10)
