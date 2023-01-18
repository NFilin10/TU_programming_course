
sonastik = {}

def kirjuta_sonastik_faili(failinimi, sonastik):
    with open(failinimi, 'w+') as fail:
        for  sona in sonastik:
            fail.write(sona + ' - ' + sonastik[sona] + "\n")


while True:
    sona = input("Sisesta sõna: ")
    if sona == "":
        kirjuta_sonastik_faili('sonad.txt', sonastik)
        print("Sõnastik kirjutati faili.")
        print("Sonas on", len(sonastik), "sona")
        break 
    
    
    if sona in sonastik:
        print(sona, 'tahendab', sonastik[sona])
    else:
        print("Sõna", sona, "sõnastikus pole")
        tahendus = input(f"Mida {sona} tähendab? ")
        sonastik[sona] = tahendus
        