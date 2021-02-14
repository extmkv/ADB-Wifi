from setuptools import setup

setup(
    name='ADB-Wifi',
    version='0.4.2',
    scripts=['adb-wifi'],
    install_requires=[
        'python-nmap',
        'netifaces',
        'netaddr'
    ]
)
