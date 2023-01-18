def loe_failist(failinimi):
    with open(failinimi) as fail:
        sisu = fail.read().strip().split("\n")
    
    loplik_sonastik = {}
    
    try:
        for i in sisu:
            toote = i.split(",")
            if toote[0] not in loplik_sonastik:
                loplik_sonastik[toote[0]] = {toote[2]: float(toote[1])}
            else:
                loplik_sonastik[toote[0]][toote[2]] = float(toote[1])
                
        return loplik_sonastik
    except:
        return loplik_sonastik
    
def valjastamine(s):
    for k, v in s.items():
        for varv, hind in v.items():
            print(f"{k} - {hind}€ ({varv})")
            
print("Kaupluses on müügil järgmised tooted: ")
valjastamine(loe_failist("hinnakiri.txt"))

tooted = loe_failist("hinnakiri.txt")
summa = 0

while True:
    ostusoov = input("Sisesta ostusoov: ")
    if ostusoov == "":
        print(f"Tasuda tuleb {summa}€")
        break
    elif ostusoov in tooted:
        varv = input("Sisesta toote värvus: ")  
        if varv not in tooted[ostusoov]:
            print(f"Sellise värvusega toodet ei ole.")
        else:
            hind = tooted[ostusoov][varv]
            summa += float(hind)
            print(f"Jooksev summa on {summa}€")
    else:
        print("Sellist toodet ei ole.")

