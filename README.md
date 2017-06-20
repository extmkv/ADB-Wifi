# ADB-Wifi
A script to auto connect to android devices in debug mode using WIFI

## Motivation
Everyday I need to connect to a lot of diferent devices to debug applications.
Some devices are USB2 and others USB3 and I lose time plugging the devices and waiting for the ADB.
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

### Created & Maintained By
[Jorge Costa](https://github.com/extmkv)
