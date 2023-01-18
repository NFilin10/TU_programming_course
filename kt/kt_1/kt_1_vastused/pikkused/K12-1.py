failinimi = input('Sisesta andmefaili nimi: ')
mees_naine = input("Kas on vaja mehi või naisi (M/N)? ").upper()
nõutud_pikkus = int(input("Sisesta minimaalne pikkus(cm): "))

with open(failinimi, encoding = "UTF-8") as fail:
    lühima_pikkus = 500
    arv = 0
    print("Sobivad kandidaadid:")
    while True:
        nimi = fail.readline().strip()
        if nimi == "":
            break
        sugu = fail.readline().strip()
        pikkus = int(fail.readline())
        if sugu == mees_naine and pikkus >= nõutud_pikkus:
            print(nimi + ' ' + str(pikkus))
            arv += 1
            if pikkus < lühima_pikkus:
                lühima_pikkus = pikkus
                
with open('sobivad.txt', 'w', encoding = "UTF-8") as g:
    if arv > 0:
        if mees_naine == "M":
            g.write(f"Valiti {arv} meest.\n")
        else:
            g.write(f"Valiti {arv} naist.\n")    
        g.write(f"Lühima sobiva kandidaadi pikkus on {lühima_pikkus} cm.\n")
    else:
        print("Sobivaid kandidaate ei ole.")
        g.write("Sobivaid kandidaate ei ole.\n")
