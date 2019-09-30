#!/usr/bin/python3 
"""Writing a simple python3 script to parse out Ip address from a flat text file"""



def main():
    try: 
        userinput = int(input("I want to find the quotient of 10/x! What is x?"))
        print(10 / userinput)


    except ZeroDivisionError: 
        print("Cannot divide by 0")

    except Exception as err:
        print("this didn't work. ERROR was " + str(err))


    else: 
        print("It worked!") 

    finally: 
        print("test complete")

#    with open("data.txt", "r") as myfile:
#        for aline in myfile:
#            for aword in aline.split():
#                ipaddress.ipaddress(aword)
        
if __name__ == "__main__":
    main()


