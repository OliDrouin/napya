#!/usr/bin/python3

import urllib.request
import json


def main():
    #r = urllib.request.urlopen('http://api.open-notify.org/astros.json')
    r2 = urllib.request.urlopen('http://api.open-notify.org/astros.json')
    #astros = r.read()
    decoded_astros = r2.read().decode('utf-8')


    #print(type(astros))
    #print(astros)
    
    print(type(decoded_astros))
    print(decoded_astros)

    print(type(json.loads(decoded_astros)))
    print(json.loads(decoded_astros))

    astros = json.loads(decoded_astros)

    for astro in astros['people']:
        print(astro['name'])


if __name__ == "__main__":
    main()
