import json
import random

def HASH(text):
    with open("D:/Tracks/Python 1/Day 19/Hash.json", "r") as textHash :
        data = json.load(textHash)
    res = ""
    for i in text :
        if i in data:
            getCR = random.choice(data[i])
            res += getCR
        else :
            res += i
    return res

def CHECKHASH(text):
    with open("D:/Tracks/Python 1/Day 19/Hash.json", "r") as textHash :
        data = json.load(textHash)

    res = ""
    check = ""
    textOFArray = []
    for i in range(0,len(text)) :
        if len(check) != 4:
            check += text[i]
        elif len(check) == 4:
            textOFArray.append(check)
            check = ""
            check += text[i]

    if check != "":
        textOFArray.append(check)

    for i in textOFArray:
        for u in data:
            if i in data[u]:
                res += u

    return res






