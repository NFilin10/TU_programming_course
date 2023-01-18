from math import pi


def koogi_hind(nimi, hind):
    if nimi == "šokolaadikook":
        hind = pi * mõõt ** 2 * 0.05
        return round(hind, 2)
    
    elif nimi == "ploomikook":
        hind = pi * mõõt ** 2 * 0.04
        return round(hind, 2)
    
    elif nimi == "Napoleoni kook":
        hind = mõõt  ** 2 * 0.08
        return round(hind, 2)
    
    else:
        
        return -1
    

nimi = str(input("Sisesta koogi nimi: "))
mõõt = float(input("Sisesta koogi mõõt: "))
if koogi_hind(nimi, mõõt) == -1:
    print("Sellist koogi pagarikoda ei valmista")
    
else:
    print("Selle koogi hind on", koogi_hind(nimi, mõõt), "eurot.")