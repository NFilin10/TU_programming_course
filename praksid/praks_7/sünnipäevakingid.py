def nimi_ja_hind(sone):
    sone = sone.split(";")
    return sone[0], float(sone[2])
    
print(nimi_ja_hind("kampsun;reedene soodusmüük;42"))

vahim = float(input("Sisesta vähim hind: "))
suurim = float(input("Sisesta suurim hind: "))
print("Sellesse hinnavahemikku jäävad järgmised kingid:")

fail = open("kingid.txt")

for i in fail.readlines():
    hind = float(i.strip().split(";")[2])
    if hind >= vahim and hind <= suurim:
        print(nimi_ja_hind(i)[0])

    