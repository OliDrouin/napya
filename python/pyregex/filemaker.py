#!/usr/bin/python3

with open("filestomake.txt", "r") as myfile:
    for fn in myfile:
        with open(fn.rstrip("\n"), "w"):
            pass
