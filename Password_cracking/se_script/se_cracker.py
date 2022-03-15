#!/usr/bin/env python3

#Useful imports:
import itertools as it
import hashlib as hl

#Constant definition:
INPUT_INFO = "input/info.txt"
INPUT_HASH = "input/hash.txt"
OUTPUT = "output/password.txt"
#Script starts here:
def main():
    try:
        with open(INPUT_HASH, mode = "r", encoding='utf-8-sig') as hash, open(INPUT_INFO, mode = "r",encoding='utf-8-sig') as info, open(OUTPUT, mode = "w",encoding='utf-8-sig') as output: #on ouvre les fichiers necessaires
            h = hash.readline().strip("\n")
            print("hash = ", h)
            information = list()
            for i in info:
                information.append(i.strip("\n"))
            password = passwd_cracker(information, h)
            if password !=0:
                output.write("Password = " + str(password).strip("\n"))
                print("Password found!")
                return 0
            else:
                print("Password Not Found")
                return 0
    except Exception as e:
        print(e)
        return 0

def passwd_cracker(information, hash):
    try:
        length = len(information)
        for i in range(1,5): #ensemble des permutations de 1 à 4 mots
            combi = list(it.permutations(information, i))
            for password in combi:
                password = str(password).translate(str.maketrans({'(': '', ')': '', ',':'', '\'':'',' ': ''}))
                password = password.strip("\n")
                hashed = hl.sha256(password.encode('utf-8')).hexdigest()
                if hash == hashed: #on teste si le hash qu'on cherche est égal au hash que l'on calcul
                    return password
                else: 
                    continue
        return 0
    except Exception as e:
        print(e)
        return 0

main()
