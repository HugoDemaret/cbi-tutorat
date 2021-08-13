#!/usr/bin/env python3

import ast
##########################
#Start of the script
##########################

# def parse(dictionary):
#     '''This function removes useless information from dictionary 
#         parse: dict -> dict
#     '''
#     try:
#         print("parse +try")
#         for i in dictionary:
#             del i["User display name"]
#             del i["Timestamp"]
#         return dictionary
#     except Exception as e:
#         print(e)
#         return "parse"
##########################
##########################

def analyse(correctDict,userDict):
    '''This function analyses and compares user inputs with correction
        analyse: dict x dict -> list
    '''
    try:
        userlist = []
        correctDict = list(correctDict)
        cdict = correctDict[0]
        for subdict in userDict:
            points = 0
            key = subdict["Email"]
            for item in cdict:
                if cdict[item] == subdict[item]:
                    points += 1
                else:
                    continue
            person = {key : points}
            userlist.append(person)
        return userlist
    except Exception as e:
        print(e)

##########################
##########################
##########################
