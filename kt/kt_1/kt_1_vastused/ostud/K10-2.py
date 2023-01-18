from math import pi, ceil

def ruumala(läbimõõt, kõrgus):
    return pi * (läbimõõt / 2)**2 * kõrgus

def soojusenergia(puuliik, ruumala):
    if puuliik == "kask":
        return 1.7 * ruumala
    elif puuliik == "mänd":
        return 1.36 * ruumala
    elif puuliik == "lepp":
        return 1.23 * ruumala
    else:
        return -1

puuliik = input("Sisesta puuliik: ")
diameeter = float(input("Sisesta diameeter meetrites: "))
kõrgus = float(input("Sisesta kõrgus meetrites: "))
if soojusenergia(puuliik, ruumala(diameeter, kõrgus)) != -1:
    print(f"See puu annab {round(soojusenergia(puuliik, ruumala(diameeter, kõrgus)),2)} MWh soojusenergiat.")
    vajadus = float(input("Mitu MWh soojusenergiat vajad? "))
    print(f"{vajadus} MWh soojusenergia jaoks on tarvis {int(ceil(vajadus/soojusenergia(puuliik, ruumala(diameeter, kõrgus))))} sellist puud.")
else:
    print("Sellise puu kohta andmed puuduvad.")
