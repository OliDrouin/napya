#!/usr/bin/python3

import requests

def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    print(r.json())

if __name__ == "__main__":
    main()
