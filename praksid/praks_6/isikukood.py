import math

def on_korrektne_isikukood(kood):
    
    summa = 0
    
    for i in range(0, 10):
        summa += int(kood[i]) * int(str(i+1)[0])

    jaak = summa % 11
    
    if jaak < 10:
        return str(jaak) == kood[-1]
    
    kaalud_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    for i in range(0, 10):
        summa += int(kood[i]) * kaalud_2[i]
    
    jaak = summa % 11
    
    if jaak < 10:
        return str(jaak) == kood[-1]    
    return "0" == kood[-1]
    
def leia_haigla(failinimi, kood):
    haigla_kood = kood[7:10]
    with open(failinimi) as fail:
        read = fail.read().strip().split("\n")
    
    haiglad = []
    vahemikud = []
    for rida in read:
        koos = rida.split(' = ')
        vahemik = koos[0]
        haigla = koos[1]
        vahemikud.append(vahemik.split("..."))
        haiglad.append(haigla)
      
    for i in range(len(vahemikud)):
        if vahemikud[i][0] <= haigla_kood and vahemikud[i][1] >= haigla_kood:
            return haiglad[i]
 
  
def leiea_sugu(kood):
    esimene_number = int(kood[0])
    if esimene_number % 2 == 0:
        return "Naine"
    return "Mees"


def leia_s_kuupaev(kood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    esimene_nr = int(kood[0])
    esimesed_kaks = str(17 + math.ceil(esimene_nr/2))
    viimased_kaks = kood[1:3]
    kuu_jr = kood[3:5]
    paev = kood[5:7]
    kuu = kuud[int(kuu_jr)-1]
    return paev+". "+kuu+" "+esimesed_kaks+viimased_kaks
    

def info_isikukoodist(kood):
    print(f"Lugesin isikukoodist {kood} välja järgmised andmed:")
    print("Sugu: ", leiea_sugu(kood))    
    print("Sunnikuupaev:", leia_s_kuupaev(kood))
    print("Haigla:", leia_haigla("haiglad.txt", kood))
    print(on_korrektne_isikukood(kood))

info_isikukoodist("50304060827")