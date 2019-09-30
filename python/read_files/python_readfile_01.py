#!/usr/bin/python3 
"""Writing a simple python3 script to parse out Ip address from a flat text file"""

def main():
    with open("data.txt", "r") as myfile:
        all_lines = myfile.readlines()

        print(all_lines)
        
if __name__ == "__main__":
    main()


