# OVPN creator
This script will create a new .ovpn file with all required information to connect a new client to your openVPN server.

## Dependencies
Before using this script, make sure that the following conditions are met when not altering the script:

- a template file called client.ovpn needs to be present in the keys folder (/etc/openvpn/easy-rsa/keys/);
- client.ovpn should not refer to any .crt, .ca, and .key files (remove or comment out the lines containing this dependency);
- client.ovpn has to contain all the contents of the .ca file between \<ca\> and \</ca\> tags.

These dependencies were based on the OpenVPN server setup instructions found on DigitalOcean: https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-14-04.

## Usage
To start, run the script. It will ask you for a device name, this name will also be used for the output file (\<device name\>.ovpn). It will then walk you through the generation of the certificate and key files. When done, the certificate and key contents are added to the .ovpn file, after which the .ovpn file will be saved in the same folder as the script.
