def loe_failist(failinimi):
    with open(failinimi) as fail:
        sisu = fail.read().strip().split("\n")
    tulemused_dict = {}
    
    for rida in sisu:
        voor, tulemus = (rida.split(";", 1))
        tulemus = tulemus.split(";")
        for i in range(0, len(tulemus)):
            tulemus[i] = int(tulemus[i])
            tulemused_dict[voor] = tulemus
    return tulemused_dict


def leia_keskmine(sonastik):
    c = 0
    
    for v in sonastik.values():
        for i in v:
            c += i

    return round(c/(len(sonastik)*len(v)),1)


fail = input("Sisesta faili nimi: ")

print("Voorude keskmised tulemused on:")
for voor, tulemused in loe_failist(fail).items():
    t = 0
    for x in tulemused:
        t += int(x)
    print(round(t/len(tulemused), 1))
print(f"Kõikide voorude keskmine tulemus on: {leia_keskmine(loe_failist(fail))}")
    
    
    