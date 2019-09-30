#!/usr/bin/python3 
"""Writing a simple python3 script to parse out Ip address from a flat text file"""



def main():
    try: 
        userinput = int(input("I want to find the quotient of 10/x! What is x?"))
        print(10 / userinput)
        x = "Successful division\n"

    except ZeroDivisionError: 
        print("Cannot divide by 0")
        x = "Zero division error\n"

    except Exception as err:
        print("this didn't work. ERROR was " + str(err))
        x = "General Error - " + str(err) + "\n"

    else: 
        print("It worked!\n") 

    finally: 
        with open("exception.log", "a") as logs:
            logs.write(x)
        print("test complete\n")

#    with open("data.txt", "r") as myfile:
#        for aline in myfile:
#            for aword in aline.split():
#                ipaddress.ipaddress(aword)
        
if __name__ == "__main__":
    main()


