import re

#121.203.197.20
#2001:0db8:0000:0000:0000:ff00:0042:8329

ipv4 = r'^(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5]).){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
ipv6 = r'^([\dA-Fa-f]{1,4}:){7}([\dA-Fa-f]{1,4})$'

input1 = int(input())
list_address = []

for i in range(input1):
    address = input()
    list_address.append(address)

for i in list_address:
    if re.fullmatch(ipv4, i):
        print("IPv4")
    elif re.fullmatch(ipv6, i):
        print("IPv6")

    else:
        print("Bukan IP Address")
