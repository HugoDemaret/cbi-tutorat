#!/usr/bin/env python3


#Useful imports:
import hashlib as hl

#Constants definition:
INPUT_HASH = "input/hash.txt"
INPUT_DICT = "input/dict.txt"
OUTPUT_PASSWD = "output/passwd.txt"
#Script begins here:
def main():
    try:
        with open(INPUT_HASH, mode="r", encoding='utf-8-sig') as hash, open(INPUT_DICT, mode="r", encoding='utf-8-sig') as dict, open(OUTPUT_PASSWD, mode="w", encoding='utf-8-sig') as output:
            h = hash.readline().strip("\n")
            for password in dict:
                password = password.strip("\n")
                hashed = hl.sha256(password.encode('utf-8')).hexdigest()
                if h == hashed:
                    output.write("Password = " + str(password))
                    print("Password found = " + password)
                    return 0
                else:
                    continue
            print("No password corresponds to your hash!")
    except Exception as e:
        print(e)
        return 0

main()
