import ipaddress
import random
import time


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


def subCalc():  # Here I am defining the subnet calculator which will be implemented in the "detention".

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

    print("Your broadcast address is: ", net4.broadcast_address)

    print("The first IPv4 address below this line, is the subnet to which a host belongs to.")

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


#  Questions in questions_answers is borrowed from the online random subnet question website "http://www.subnettingquestions.com"

questions_answers = (('What is the broadcast address of the network 172.21.213.192 255.255.255.224?', '172.21.213.223'),

                    ('What is the broadcast address of the network 172.27.154.128 255.255.255.128?', '172.27.154.255'),

                    (' What is the first valid host on the subnetwork that the node 192.168.175.74/27 belongs to?', '192.168.175.65'),

                    ('What is the first valid host on the subnetwork that the node 172.17.123.213 255.255.255.240 belongs to?', '172.17.123.209'),

                    ('What is the broadcast address of the network 192.168.168.192 255.255.255.192?', '192.168.168.255'),

                    ('What is the last valid host on the subnetwork 172.27.48.0 255.255.240.0?', '172.27.63.254'),

                    ('What is the broadcast address of the network 172.21.85.192/26?', '172.21.85.255'),

                    ('What is the last valid host on the subnetwork 10.214.96.0 255.255.240.0?', '10.214.111.254'),

                    ('What is the first valid host on the subnetwork that the node 172.17.72.251 255.255.255.224 belongs to?', '172.17.72.225'),

                    ('What is the broadcast address of the network 172.31.152.128/25?', '172.31.152.255'),

                    ('What valid host range is the IP address 172.21.15.239/27 a part of?', '172.21.15.225 to 172.21.15.254'),

                    ('What is the broadcast address of the network 172.20.112.0 255.255.248.0?', '172.20.119.255'),

                    ('What is the first valid host on the subnetwork that the node 172.18.46.26/23 belongs to?', '172.18.46.1'),

                    ('What is the broadcast address of the network 172.29.189.128/26?', '172.29.189.191'),

                    ('What valid host range is the IP address 172.31.102.168/24 a part of?', '172.31.102.1 to 172.31.102.254'),

                    ('Which subnet does host 10.59.237.118 255.255.240.0 belong to?', '10.59.224.0'),

                    ('What valid host range is the IP address 192.168.121.206/26 a part of?', '192.168.121.193 to 192.168.121.254'),

                    ('What is the last valid host on the subnetwork 172.19.240.0 255.255.240.0?', '172.19.255.254'),

                    ('What is the first valid host on the subnetwork that the node 192.168.154.253/25 belongs to?', '192.168.154.129'),

                    ('What is the first valid host on the subnetwork that the node 192.168.219.53 255.255.255.248 belongs to?', '192.168.219.49'),

                    ('What valid host range is the IP address 172.16.182.71/21 a part of?', '172.16.176.1 to 172.16.183.254'),

                    ('What is the last valid host on the subnetwork 172.23.179.32 255.255.255.240?', '172.23.179.46'),

                    ('What is the first valid host on the subnetwork that the node 10.114.18.231 255.255.240.0 belongs to?', '10.114.16.1'),

                    ('Which subnet does host 192.168.58.12 255.255.255.248 belong to?', '192.168.58.8'),

                    ('What valid host range is the IP address 172.29.64.219/23 a part of?', '172.29.64.1 to 172.29.65.254'),

                    ('What is the first valid host on the subnetwork that the node 172.21.138.153/23 belongs to?', '172.21.138.1'),

                    ('Which subnet does host 192.168.158.13/27 belong to?', '192.168.158.0'),

                    ('What is the broadcast address of the network 192.168.117.128/25?', '192.168.117.255'),

                    ('What is the broadcast address of the network 172.29.160.0/20?', '172.29.175.255'),

                    ('What is the first valid host on the subnetwork that the node 172.22.203.247 255.255.255.128 belongs to?', '172.22.203.129'),

                    ('What is the last valid host on the subnetwork 172.19.8.0 255.255.255.128?', '172.19.8.126'),

                    ('What is the last valid host on the subnetwork 192.168.109.184/30?', '192.168.109.186'),

                    ('What is the first valid host on the subnetwork that the node 172.16.29.250/22 belongs to?', '172.16.28.1'),

                    ('What is the last valid host on the subnetwork 172.17.164.0/22?', '172.17.167.254'),

                    ('What is the broadcast address of the network 172.18.28.0/23?', '172.18.29.255'),

                    ('What is the broadcast address of the network 172.19.24.0/21?', '172.19.31.255'),

                    ('What is the broadcast address of the network 192.168.205.32/28?', '192.168.205.47'),

                    ('Which subnet does host 10.34.185.54 255.255.240.0 belong to?', '10.34.176.0'),

                    ('What is the broadcast address of the network 172.19.149.192/27?', '172.19.149.223'),

                    ('What is the first valid host on the subnetwork that the node 172.26.197.148/26 belongs to?', '172.26.197.129'))


def subDet(x, y):  # Defining the detention function - x is tries, and y is question counter
    triesDet = x
    correctDet = 0
    correctTgt = y

    if triesDet != 0:
        print("Welcome to the detention.")
        time.sleep(1)
        print("Here you must answer", correctTgt, "subnetting questions correct in a row.")
        time.sleep(1)
        print("But worry not. You will be aided by a trustworthy subnet calculator.")
        time.sleep(1)
        print("But take care when you answer the questions - if you give an incorrect answer, you must start over.")
        time.sleep(1)
    elif triesDet == 0:
        print("Welcome to the detention. You have no more lives, and are stuck here for all your text based life.")
        time.sleep(1)

    while correctDet is not correctTgt:
        word_subDet = random.choice(questions_answers)
        questionDet = word_subDet[0]
        answerDet = word_subDet[1]

        if triesDet == 0:
            print(questionDet)
            time.sleep(1)
            guess = input("Please type your answer here:\n")

            if guess == answerDet:
                print("Success - Succeeded")

            elif guess != answerDet:
                print("You've entered a wrong answer.")

        while True and triesDet != 0:
            print(questionDet)
            time.sleep(1)
            subCalc()
            guess = input("Please type your answer here:\n")
            if guess == answerDet:
                print("Success - Succeeded")
                correctDet += 1
                print("You have this many questions to go: ", (correctTgt-correctDet))
                break

            elif guess != answerDet:
                correctDet = 0
                correctTgt = y
                print("You've entered a wrong answer - the counter has reset, and you must answer", correctTgt, "correct in a row.")
                break
        if correctDet == correctTgt:
            print("Congratulations, you've successfully answered", correctTgt, "questions in a row - you may now leave.")
            break


def subChall():

    lives = 3
    tries = 3
    correct = 0
    question_counter = 5

    print("Welcome to the Subnet challenge.\nHere you will be presented with a question, and you must type in your "
          "answer.")
    time.sleep(1)
    print("If you get 5 correct, you win and may continue to the next room.")
    time.sleep(1)
    print("But beware. If you fail 3 times, you will go to 'Detention', where you must answer 5 questions "
          "correctly.\nIn 'Detention' you will be aided by a subnet calculator.")
    time.sleep(1)
    print("If you lose all 3 lives again, you will once again go to 'Detention'. Only, now you must answer 10 "
          "correctly, to get out.")
    time.sleep(1)
    print("Should you lose your 3 lives once again, you will be sent to 'Detention', and may never come out.")
    time.sleep(1)
    print("You will be answering subnetting questions for all of your eternal text-based life.")
    time.sleep(2)

    for x in range(5):
        word_sub = random.choice(questions_answers)
        question = word_sub[0]
        answer = word_sub[1]
        while True:
            print(question)
            guess = input("Please type your answer here:\n")

            if guess == answer:
                print("Success - Succeeded")
                question_counter -= 1
                print("Questions left: ", question_counter)
                break

            elif guess != answer:
                lives -= 1
                if lives == 0:
                    tries -= 1
                    lives = 3
                    print("You've lost, and will be sent to detention.")
                    print("You have", tries, "tries left.")
                    time.sleep(2)
                    if tries == 2:
                        subDet(tries, 5)
                    elif tries == 1:
                        subDet(tries, 10)
                    elif tries == 0:
                        subDet(tries, 15)
                    break
                else:
                    print("Incorrect answer - try again")
                    print("lives left:", lives)
                    continue
        if question_counter == 0:
            print("Congratulations, you've successfully answered 5 questions - you may now leave.")
            break
