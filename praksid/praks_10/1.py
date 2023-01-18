
def failist_sõnastikku(failinimi):
    with open(failinimi) as fail:
        read = fail.read().strip().split("\n")
        
    sonastik = {}

    for rida in read:
        rida = rida.split()
        sonastik[rida[0]] = rida[1]
        
    return sonastik


def koodid_nimedeks(failinimi, sonastik):
    with open(failinimi) as fail:
        read = fail.read().strip().split("\n")
        
    jrj = []

    for rida in read:
        if rida in sonastik:
            jrj.append(sonastik[rida])
        else:
            jrj.append("Tundmatu")
    return jrj

    

fail1 = input("Sisesta riigikoodide faili nimi: ")
fail2 =input("Sisesta piiriületuste faili nimi: ")


riigid = koodid_nimedeks(fail2, failist_sõnastikku(fail1))

for i in riigid:
    print(i)