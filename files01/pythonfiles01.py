#!/usr/bin/python3

def main():
    myfile = open("example.txt", "w")
    print("what's up", file=myfile, end="\n")

    myfile.write("Konnichiwa\n")
    myfile.close()

    with open("example02.txt", "w") as myfile:
        myfile.write("This is great\n") 
        print("we can still write from ehre", file=myfile, end="\n")

if __name__ == "__main__":
    main()

