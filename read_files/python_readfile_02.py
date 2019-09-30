#!/usr/bin/python3 
"""Writing a simple python3 script to parse out Ip address from a flat text file"""

import ipaddress

def main():
    with open("data.txt", "r") as myfile:
        for aline in myfile:
            for aword in aline.split():
                try:
                    ipaddress.ip_address(aword)
                    with open("data_ips.txt", "a") as ips: 
                        ips.write(aword + "\n")
                except:
                    pass



if __name__ == "__main__":
    main()


