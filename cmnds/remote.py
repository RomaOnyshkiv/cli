import os
import subprocess
import paramiko


def run_ssh_command(cmd, server, usr, pswd):
    password = os.environ["REMOTE_PASS"] if (pswd is None) else pswd
    r_user = os.environ["REMOTE_USER"] if (usr is None) else usr
    r_server = os.environ["REMOTE_SERVER"] if (server is None) else server
    results = subprocess.run(("sshpass", "-p", password, "ssh", f'{r_user}@{r_server}', cmd))
    print(f'Exit code: {results.returncode}')


def get_remote_session(pswd):
    password = os.environ["REMOTE_PASS"] if (pswd is None) else pswd


def run_on_remote(host, pwd, usr, command, file):
    pswd = os.environ["REMOTE_PASS"] if (pwd is None) else pwd
    r_user = os.environ["REMOTE_USER"] if (usr is None) else usr
    r_server = os.environ["REMOTE_SERVER"] if (host is None) else host
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=r_server, username=r_user, password=pswd)
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
