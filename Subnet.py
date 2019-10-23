# Class A - 1.0.0.1 to 126.255.255.254 || Default Subnet Mask 255.0.0.0
# Class B - 128.1.0.1 to 191.255.255.254 || Default Subnet Mask 255.255.0.0
# Class C - 192.0.1.1 to 223.255.254.254 || Default Subnet Mask 255.255.255.0

from random import getrandbits
from ipaddress import IPv4Address

import ipaddress
# - Random IP Address generator

bits = getrandbits(32)
address = IPv4Address(bits)
str_address = str(address)

print(str_address)

# - Question generator

IP = input("Enter IPv4 address here: ")
MASK = '255.255.0.0'

host = ipaddress.IPv4Address(IP)
net = ipaddress.IPv4Network(IP + '/' + MASK, False)
print('IP:', IP)
print('Mask:', MASK)
print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast:', net.broadcast_address)