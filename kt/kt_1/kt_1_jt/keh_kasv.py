fail = input("Sisesta andmefaili nimi: ")
fail = open(fail)

hinne = int(input("Sisesta hinne: "))
tundide_arv = int(input("Sisesta tundide arv: "))

opilasi_kokku = 0
sobivaid_opilasi = 0
keskmine_hinne = 0

print(f"Õpilased, kelle hinne on {hinne} ja kes osalesid vähemalt {tundide_arv} tunnis:")


while True:
    nimi = fail.readline().strip()
    print(nimi)
    if nimi == "":
        break
    opilasi_kokku += 1

    hinne_failis = float(fail.readline().strip())
    keskmine_hinne += hinne_failis
    hinne_failis_ümar = round(hinne_failis)
    osalemine = int(fail.readline().strip())

    if hinne_failis_ümar == hinne and tundide_arv <= osalemine:
        print(nimi, osalemine)
        sobivaid_opilasi += 1
    

sobivad = open("sobivad.txt", "w")

if sobivaid_opilasi == 0:
    print("Sobivaid õpilasi ei ole.")
    sobivad.write(f"Klassis on {opilasi_kokku} õpilast, nende keskmine hinne on {round(keskmine_hinne/opilasi_kokku, 2)}.\nSobivaid õpilasi ei ole.")

else:
    sobivad.write(f"Klassis on {opilasi_kokku} õpilast, nende keskmine hinne on {round(keskmine_hinne/opilasi_kokku, 2)}.\nSobivaid õpilasi on {sobivaid_opilasi}.")

fail.close()
sobivad.close()