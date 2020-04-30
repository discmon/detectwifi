# detectwifi

This version will be deployed at Amoy Quee Camp as part of tracking efforts during COVID-19.
Steps to install this system:
After running the usual apt-get update & upgrades, we will need to change the system to kali headers in order to set the Wifi Modules to monitor mode.

cd /usr/local/src
sudo wget -O re4son-kernel_current.tar.xz https://re4son-kernel.com/download/re4son-kernel-current/
sudo tar -xJf re4son-kernel-current.tar.xz
cd into the extracted directory
sudo ./install.sh

Set up the environment:
sudo apt-get install aircrack-ng python git python-setuptools net-tools ntp
git clone https://github.com/drkjam/netaddr
cd netaddr
sudo python setup.py install

git clone https://github.com/secdev/scapy.git
cd scapy
sudo python setup.py install

Now go into the downloaded repository and do the following edits:
Go to cmd and run ifconfig.
Choose the WiFi interface to be used, and note down the name.
Then run sudo airmon-ng start <interface name> and note down the new interface name using ifconfig.

In probe: Set the node name by changing AP1, change the interface names accordingly to match airmon-ng operations
In probemon.py: Change the node name by changing AP1
In batch_upload: Set the node name by changing AP1

Execute crontab -e and insert the following lines:
*/2 0-2,4-23 * * * /bin/bash -c [full path to probe] #Triggers the detection every 2 minutes except at 3am
0 3 * * * /bin/bash -c [full path to batch_upload] #Allows for batch uploading at 3am
50 3 * * * rm /home/pi/probemon/logs/* #Wipes all the logs for the day at 3am
