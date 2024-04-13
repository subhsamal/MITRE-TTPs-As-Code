The repo contains codes for cybersecurity tasks/automations that I have learned over the time. 


# To install dependencies:
python -m pip install -r requirements.txt


I am using Brython module to run python script for webpages. Brython is designed to replace Javascript as the scripting 
language for the Web. You can download bython files from their repo and keep in your repo. 
https://github.com/brython-dev/brython/releases


# What is happening
Project:1 [Tactic: Execution]
* Attacker runs a server on target users system
* Tricks user to open a webpage and captures credentials once entered
* Through the script within webpage, the credentials are sent to attacker or printed on the console.
* Attacker may run a scheduler code to run the server randomly (to be done)

Project:2 [Tactic: Privilege Escalation]
* Attacker may trick user to do a process injection
* They may link the suspicious code to a boot time program, since it runs with system permission. 


# Credit
My work is inspired from the following
1. Python for Cybersecurity Specialization - Coursera 


# References
https://github.com/hposton/python-for-cybersecurity