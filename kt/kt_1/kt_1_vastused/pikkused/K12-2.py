from math import ceil

def arvuta_kulu(km, kütusekulu, hind):
    return round(km * kütusekulu * hind / 100, 2)

def arvuta_sõiduhind(aeg, kütuse_raha):
    if aeg <= 30:
        return ceil(0.3 * aeg + kütuse_raha)
    elif aeg <= 60:
        return ceil(0.2 * aeg + kütuse_raha)
    else:
        return ceil(0.1 * aeg + kütuse_raha)

km = float(input("Sisesta läbitud kilomeetrite arv: "))
aeg = int(input("Sisesta kulunud aeg minutites: "))
kütusekulu = float(input("Sisesta auto kütusekulu (l/100km): "))
kütuse_hind = float(input("Sisesta kütuse hind tanklas: "))
print(f"Kütusele kulus {arvuta_kulu(km, kütusekulu, kütuse_hind)} eurot.")
print(f"Sõidu hind kokku on {arvuta_sõiduhind(aeg, arvuta_kulu(km, kütusekulu, kütuse_hind))} eurot.")
