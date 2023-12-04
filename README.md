# block_internet
<b>`block internet access to specified program.`</b>
<br>
<br>You need to have python and <b>psutil</b> library, that's it.<br>

<br>Run the program you want to block, then execute the <b>"python block_internet.py"</b> enter the <b>"app name"</b> you want to block.
<br>block_internet will determine the <b>PID</b> for the given program name and using IPTABLE it will block all traffics for it.
<br>
If you are using "firewalld", `block_internet` will change "firewalld" to ![DISABLE](https://img.shields.io/badge/status-DISABLED-red)  before adding the rules for "iptable" as long as the program is running.
<br> if you have firewalld configured for traffic or security purpose please consider other solution :)


<br> Hitting <b>"Enter"</b> will restore the settings and internet traffic will be allowed for the program.



have fun.
