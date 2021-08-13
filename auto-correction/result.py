#!/usr/bin/env python3

#Constants:
OUTPUT="output/results.txt"

#Script starts here:
##########################
def result(userlist):
    '''This function prints the output result in a file
        result: list -> string
    '''
    try:
        with open(OUTPUT, mode='w', encoding='utf-8-sig') as output:
            for item in userlist:
                output.write(str(item).translate(str.maketrans({'{': '', '}': '', '\'' : ''})) + "\n")
    except Exception as e:
        print(e)

##########################
##########################
##########################
