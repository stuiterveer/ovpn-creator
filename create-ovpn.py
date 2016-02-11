#!/usr/bin/python

import os

if os.geteuid() != 0:
    exit("Please run this script as root!")

scriptDir =  os.getcwd()
os.chdir("/etc/openvpn/easy-rsa")

deviceName = raw_input("Please input the name for the certificate you're generating: ")
os.system(". ./vars && ./build-key " + deviceName)
os.chdir("keys")
os.system("cp client.ovpn %s/%s.ovpn" %(scriptDir, deviceName))

certFile = open(deviceName + ".crt", "r")
cert =  certFile.read()
certFile.close

keyFile = open(deviceName + ".key", "r")
key =  keyFile.read()
keyFile.close

os.chdir(scriptDir)

ovpnFile = open(deviceName + ".ovpn", "a")
ovpnFile.write("\n<cert>\n%s</cert>\n<key>\n%s</key>\n" %(cert, key))
ovpnFile.close()
