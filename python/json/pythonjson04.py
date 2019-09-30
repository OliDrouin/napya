#!/usr/bin/python3

import requests

def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    astros = r.json()

    print(astros['people'])
    for astro in astros['people']:
        print(astro['name'].split()[0])

    with open('inventory', "w") as fh:
        for astro in astros['people']:
            print(astro['name'].split()[0], file=fh, end="\n")



if __name__ == "__main__":
    main()
