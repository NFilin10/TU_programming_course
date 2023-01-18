import string
import random

def suurväike(sõne):
    rand_punct = string.punctuation[random.randint(0, len(string.punctuation))]
    
    sõne_list = list(sõne)
    
    for i in range(0, len(sõne_list)):
        if sõne_list[i].isupper():
            sõne_list[i] = sõne_list[i].lower()
        elif sõne_list[i].islower():
            sõne_list[i] = sõne_list[i].upper()
        elif sõne_list[i] in string.punctuation:
            sõne_list[i] = str(rand_punct)
    return "".join(sõne_list)

faili_nimi = input("Sisesta faili nimi: ")
fail = open(faili_nimi)
sisu = fail.readlines()

for i in sisu:
    print(suurväike(i).strip())
fail.close()