from urllib.request import urlopen
def loe_saladus(url, algus, lõpp):
    allikas = urlopen(url)
    baidid = allikas.read()
    tekst = baidid.decode()
    
    index = tekst.find(algus) + len(algus)
    index2 = tekst.find(lõpp)
    
    sõne = []
    
    for i in range(index, index2):
        sõne.append(tekst[i])
    return "".join(sõne)
print(loe_saladus("https://courses.cs.ut.ee/2022/programmeerimine/fall/Main/Kodu5", "ylisalajane:", ":ylisalajane"))