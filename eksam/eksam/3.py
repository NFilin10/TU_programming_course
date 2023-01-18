def loe_seis(fail):
    with open(fail) as f:
        sisu = f.read().strip().split("\n")
    formatted_sisu = sisu[1:]
    
    sonastik = {}
    
    for i in formatted_sisu:
        sonastik[i.split()[0]] = i.split()[1:]

    converted_dict = {}
    dict_val = []
    
    for k, v in sonastik.items():
        for i in range(len(v)):
            if v[i] != "-":
                dict_val.append(int(v[i]))
                
                
            else:
                dict_val.append(v[i])
            converted_dict[k] = dict_val
        dict_val = []
            
    
    return converted_dict
    

def lisa_tulemus(nimi, mangu_nr, sonastik, tulemus):
    if sonastik.get(nimi):
        mangija_tulemused = sonastik[nimi]
        if mangu_nr > len(mangija_tulemused):
            print("Sellist mängu numbrit ei ole")
        
        else:
            vastav_mangu_tulemus = mangija_tulemused[mangu_nr-1]
            
            if vastav_mangu_tulemus == "-":
                (sonastik[nimi])[mangu_nr-1] = tulemus
                print("Tulemus lisatud")
            else:
                print("Tulemus juba olemas")
            
    else:
        print("Sellise nimega korvpalluri kohta andmeid pole")
        
        
def leia_keskmine(nimi, sonastik):
    mangija_tulemused = sonastik[nimi]
    
    ainult_punktid = []
    
    for i in mangija_tulemused:
        if type(i) == int:
            ainult_punktid.append(i)
    
    return sum(ainult_punktid)/len(ainult_punktid)


def leia_parim(sonastik):
    parim = 0
    tulemused = []
    nimed = {}
    
    for k, v in sonastik.items():
        nimi, keskmine = (k, leia_keskmine(k, sonastik))
        tulemused.append(keskmine)
        nimed[keskmine] = nimi
        
    parim = max(tulemused)
    parima_nimi = nimed.get(parim)
    return f"Parim on {parima_nimi} tulemusega {parim}"
        


sonastik = loe_seis("korvpall.txt")
while True:
    print('''
1 - Vaata punktitabelit
2 - Lisa tulemus
3 - Leia korvpalluri keskmine
4 - Leia parim
5 - Lõpeta programmi töö''')

    kasutaja_valik = input("Vali tegevus: ")

    if kasutaja_valik == "1":
        for k, v in sonastik.items():
            print(k, " ".join(map(str, v)))
            
    if kasutaja_valik == "2":
        nimi = input("Sisesta nimi: ")
        mangu_nr = int(input("Sisesta mängu järjekorra number: "))
        punktid = int(input("Sisesta punktid: "))
        lisa_tulemus(nimi, mangu_nr, sonastik, punktid)
    
    if kasutaja_valik == "3":
        nimi = input("Sisetsa nimi: ")
        print(f"{nimi} keskmine skoor on {leia_keskmine(nimi, sonastik)}")
        
    if kasutaja_valik == "4":
        print(leia_parim(sonastik))
        
    if kasutaja_valik == "5":
        with open("korvpall.txt") as f:
            sisu = f.read().strip().split("\n")
        sisu_faili = 5*" "+ "".join(sisu[0])
        
        with open("korvpall_uus.txt", "w") as fail:
            fail.write(sisu_faili+"\n")
            for k, v in sonastik.items():
                fail.write(k + " " + " ".join(map(str, v))+"\n")
        print("Programm lõpetas töö.")
        break 
        
        
    