#!/usr/bin/env python3
from hashlib import md5
from util import postData
import subprocess

def getLocalIp():
    ip = subprocess.run("hostname -I", stdout=subprocess.PIPE, shell=True)
    ip = ip.stdout.decode('utf-8')
    return ip.split(' ')[0]

def main():
    postData('data/ip', { "ip": getLocalIp() })

if __name__ == "__main__":
    main()


