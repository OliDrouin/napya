#!/usr/bin/python3

import os
import sys
import argparse
import json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()


        if self.args.list:
            self.inventory = self.example_inventory()
    
        elif self.args.host:
            self.inventory = self.empty_inventory()

        else: 
            self.inventory = self.empty_inventory()

    
        print(json.dumps(self.inventory))

    
    def example_inventory(self):
        return {
            'group': {
                'hosts': ['bender', 'fry'],
                'vars': {
                    'example_var1': 'proxyeast',
                    'example_var2': 'proxywest'
                }
            }, 
            '_meta': {
                'hostvars': {
                    'bender': {
                        'ansible_ssh_user': 'bender',
                        'ansible_host': '10.10.2.3'
                
                    },
                    'fry': {
                        'ansible_ssh_user': 'fry',
                        'ansible_host': '10.10.2.4'
                    
                    }

                }       
            }
        }

    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

ExampleInventory()
