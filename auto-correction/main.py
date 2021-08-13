#!/usr/bin/env python3

#Useful imports
from analyse import analyse
from result import result
import csv
##########################
#Start of the main script
##########################
def main():
    try:
        with open("input/correction.csv",mode = "r", encoding='utf-8-sig') as correction, open("input/userinput.csv",mode = "r", encoding='utf-8-sig') as userInput:
            correctDict = csv.DictReader(correction)
            userDict = csv.DictReader(userInput)
            # print(list(correctDict),"     correctdict\n")
            # print(list(userDict),"    Userdict\n")
            userlist = analyse(correctDict,userDict)
            result(userlist)
    except Exception:
        return "main"
##########################
##########################

main()

##########################
#######End of script######
##########################
