#!/usr/bin/python3

import re
import os

for odfile in os.listdir():
    matched = re.search(r'^.*(2018-[01]\d-[0-3]\d).*$', odfile)
    if matched:
        #print(odfile)
        print(matched.group(0))
        print(matched.group(1))


        with open(odfile) as goodips:
            ips = goodips.read()

        newfilename = matched.group(1) + ".txt"

        with open("output/" + newfilename, "w") as newfile:
            newfile.write(ips)

        with open("output/" + "2018ips.txt", "a") as masterips:
            masterips.write(ips)
