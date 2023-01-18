import random

def loe_sonad_failist(failinimi):
    sonastik = {}
    with open(failinimi) as fail:
        read = fail.read().strip().split("\n")
        
    for rida in read:
        sona, tahendus = rida.split(" - ")
        sonastik[sona] = tahendus
    return sonastik

sonastik = loe_sonad_failist('sonad.txt')

punktid = 0

votmed = list(sonastik)

while True:
    if punktid == 10:
        print("SA VÕITSID, VÄGA TUBLI!")
        break
    if punktid == -10:
        print("sa kaotasid")
        break
    suvaline = random.choice(votmed)
    
    vastus = input("Mida tahendab " + suvaline + "? ")
    
    if sonastik[suvaline] == vastus:
        print("Oige")
        punktid += 1
    else:
        print("Vale")
        punktid -= 1