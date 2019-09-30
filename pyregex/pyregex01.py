#!/usr/bin/python3

import re
import os

for odfile in os.listdir():
    matched = re.search(r'^.*(2018-[01]\d-[0-3]\d).*$', odfile)
    if matched:
        print(odfile)

