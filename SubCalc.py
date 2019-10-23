import ipaddress


def validate_ip(self):  # Here I am defining the function, that will check the validity of the users input
    a = self.split('.')
    if len(a) != 4:
        return False
    for x1 in a:
        if not x1.isdigit():
            return False
        i = int(x1)
        if i < 0 or i > 255:
            return False
    return True


while True:  # Here the user inputs an IPv4 address, which is checked by the validate_ip function
    ip_addr = input("Type in IPv4 address: ")
    if validate_ip(ip_addr):
        break
    else:
        print("Invalid IPv4 address - try again")

while True:  # Here I am checking if the CIDR prefix is within a desirable range (1-30)
    try:
        answer = str(input("Would you like to input a subnet prefix, or the whole netmask? prefix/netmask\n"))
    except ValueError:
        continue
    if not answer.lower() == "prefix":
        if not answer.lower() == "netmask":
            print("Please input 'prefix' or 'netmask' for me to understand.")
            continue
        else:
            netmask = input("Type your netmask here: ")
            if validate_ip(netmask):
                ip_pref = (sum(bin(int(x)).count('1') for x in netmask.split('.')))
                checkNetmask = ""
                checkNetmask = ip_addr + ("/" + str(ip_pref))
                try:
                    first_validhost = str(ipaddress.IPv4Network(checkNetmask, False)[1])
                except IndexError:
                    print("Address is out of range, try a smaller netmask")
                    continue
                break
            else:
                print("Invalid netmask address - try again")
    else:
        try:
            ip_pref = int(input("Type in your prefix: /"))
            if ip_pref < 1 or ip_pref > 30:
                raise ValueError
            break
        except ValueError:
            print("Invalid prefix - please input a prefix in the range 1-30")
            continue
        break

ip_pref2 = "/" + str(ip_pref)
ip_input = (ip_addr + ip_pref2)

net4 = ipaddress.IPv4Network(ip_input, False)
first_validhost = str(net4[1])
last_validhost = str(net4[-2])

print("Your subnet mask is: ", net4.netmask)
print("Your total amount of host addresses are: ", net4.num_addresses)
print("Your total amount of usable host addresses are: ", net4.num_addresses-2)
print(list(net4.subnets()))
while True:  # This segment prints which type of address the user has inputted.
    if net4.is_global:
        print("This is a global address.")
        break
    elif net4.is_private:
        print("This is a private address.")
        break
    elif net4.is_multicast:
        print("This is a multicast address.")
        break
    elif net4.is_unspecified:
        print("This is an unspecified address.")
        break
    elif net4.is_reserved:
        print("This is a reserved address.")
        break
    elif net4.is_loopback:
        print("This is a loopback address.")
        break
    elif net4.is_link_local:
        print("This is a link-local address.")
        break

while True:
    try:
        answer = str(input("Would you like a list of all host addresses in your subnet? Yes/No\n"))
    except ValueError:
        continue
    if not answer.lower() == "yes":
        if not answer.lower() == "no":
            print("Please input 'yes' or 'no' for me to understand.")
            continue
        else:
            print("As you wish.")
            break
    else:
        for x in net4.hosts():
            print(x)
        break

while True:
    try:
        answer = str(input("Would you like to know the first and last valid host on the subnetwork? Yes/No\n"))
    except ValueError:
        continue
    if not answer.lower() == "yes":
        if not answer.lower() == "no":
            print("Please input 'yes' or 'no' for me to understand.")
            continue
        else:
            print("As you wish.")
            break
    else:
        print("Your first valid host is: ", first_validhost)
        print("Your last valid host is: ", last_validhost)
        break
