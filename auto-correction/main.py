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
            userlist = analyse(correctDict,userDict)
            result(userlist)
    except Exception as e:
        print(e)
##########################
##########################

main()

##########################
#######End of script######
##########################
