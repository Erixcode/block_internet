# block_internet
block internet access to specified program.
You need to have python and psutil library, that's it.

run the program you want to block,then execute the block_internet.py enter the app name you want to block, block_internet will determine the PID for the given program name and using IPTABLE it will block all traffics for it.
if you are using "firewalld", block_internet will disable "firewalld" before adding the rules for "iptable" as long as the program is running. hitting Enter will restore the settings and internet traffic will be allowed for the program.



have fun.
