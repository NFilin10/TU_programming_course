from random import choice

def mängi(valik_1, valik_2):
    if valik_1 == "kivi" and valik_2 == "käärid":
        return "esimene"
    elif valik_1 == "paber" and valik_2 == "kivi":
        return "esimene"
    elif  valik_1 == "käärid" and valik_2 == "paber":
        return "esimene"
    elif valik_1 == valik_2:
        return  "viik"
    else:
        return "teine"

valikud = ["kivi", "paber", "käärid"]
counter = 0

minu_voit = 0
arvuti_voit = 0

while counter < 3:
    valik_1 = input("Sisesta oma valik: ")
    valik_2 = choice(valikud)
    if mängi(valik_1, valik_2) == "esimene":
        minu_voit += 1
        print(f"Arvuti valis {valik_2}. Sina võitsid! Sina {minu_voit}, arvuti {arvuti_voit}. ")
    
    elif mängi(valik_1, valik_2) == "teine":
        arvuti_voit += 1
        print(f"Arvuti valis {valik_2}. Arvuti võitis! Sina {minu_voit}, arvuti {arvuti_voit}. ")
        
    elif mängi(valik_1, valik_2) == "viik":
        print(f"Arvuti valis {valik_2}. Viik! Sina {minu_voit}, arvuti {arvuti_voit}. ")
    counter += 1

if minu_voit == arvuti_voit:
    print("Mäng jäi viiki!")
    
elif minu_voit > arvuti_voit:
    print("Sina võitsid!")
    
elif minu_voit < arvuti_voit:
    print("Arvuti võitis!")


    