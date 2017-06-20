# ADB-Wifi
A script to automatically connect android devices in debug mode using WIFI 
 
<p align="center">
<img src="extras/example.gif" width="100%" />
</p>

## Motivation
Everyday I need to connect to a lot of diferent devices to debug applications.
Some devices are Micro-USB and others USB Type-C and I lose time plugging the devices and waiting for the ADB.
So, I created this script to auto connect to a device using WIFI. 
**The diference to the other script and plugins:** The script save the connections in a configuration file to try reconnect when you boot your computer or when your device lost the wifi connection.

## Requirements
* Python 2.7
* ADB

## Usage
```bash
python2.7 adb_wifi.py
``` 
Add the script to your ```~/.bash_profile``` or ```~/.bash_profile``` if you are using OSX.

Connect the devices to your computer and authorized the debub.

**Attention:** If your device turns off(battery, etc), you need to plug again the device to the computer because the adb need to open the ```tcpip port```!  
If your device has rooted you can use this [application](https://play.google.com/store/apps/details?id=com.ttxapps.wifiadb)
 to turn on the ```tcpip port```and ignore this step.

### Created & Maintained By
[Jorge Costa](https://github.com/extmkv)
