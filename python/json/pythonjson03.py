#!/usr/bin/python3

import requests

def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    astros = r.json()

    print(astros['people'])

if __name__ == "__main__":
    main()
