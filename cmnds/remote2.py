import os
import paramiko


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
        bash_script = open(file).read()
        stdin, stdout, stderr = client.exec_command(bash_script)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)

    if command:
        print("=" * 50, command, "=" * 50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)

    client.close()

    print("done")


def run_script(host, pwd, usr, file):
    pswd = os.environ["REMOTE_PASS"] if (pwd is None) else pwd
    commands = [
        "pwd",
        "ls -lah",
        "cat renew"
    ]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=usr, password=pswd)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    bash_script = open(file).read()
    stdin, stdout, stderr = client.exec_command(bash_script)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)
    client.close()

    print("done")