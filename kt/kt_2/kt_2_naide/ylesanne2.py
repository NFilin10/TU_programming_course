def loe_tulemused(failinimi):
    with open(failinimi) as fail:
        sisu = fail.read().strip().split("\n")
    
    tulemused = []
    
    for tulemus in sisu:
        tulemused.append(tulemus.split(";"))
    return tulemused


def kes_võitis(jrj):
    voite = []
    for i in jrj:
        voite.append(i.count("V"))
    return voite.index(max(voite))+1

failinimi = input("Sisestage failinimi: ")
print(f"Turniiri võitis {kes_võitis(loe_tulemused(failinimi))}. võistkond.")