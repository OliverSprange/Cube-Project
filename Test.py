import random

def rand_sub():
        sub_question = (sum(bin(int(x)).count('1') for x in rand_sub.split('.')))
        checkNetmask = ""
        checkNetmask = ip_addr + ("/" + str(ip_pref))

list = [128,255, 254, 127]
#  Borrowed by user jonrsharpe - posted at https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-as-string
def rand_ip():
    ip_question = ".".join(map(str, (random.list(0,255)
    for _ in range (4))))
    return ip_question
rand_ip()