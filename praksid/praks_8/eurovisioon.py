
sisend = "Austria, 12, 6, 3, 3, 4, 7, 5, 3, 12, 8, 4, 3"

def riik(rida):
    rida = rida.split(",")
    return rida[0]
    
    
sisend2 = "Prantsusmaa, 1, 5, 2, 12, 2, , 4, 7, , 12, 12, 6"
    
def summa(rida):
    skoorid = rida.split(",")[1:]
    summa = 0
    
    for i in range(len(skoorid)):
        if skoorid[i].strip() == '':
            continue
        else:
            summa += int(skoorid[i])
            
    return summa 
    
    
failinimi = input("Sisesta failinimi: ")
with open(failinimi) as fail:
    riigid = fail.read().strip().split("\n")
    
    voitja = ""
    suurim_skoor = 0
    
    for rida in riigid:
        riigi_nimi = riik(rida)
        riigi_skoor = summa(rida)
        
        if riigi_skoor > suurim_skoor:
            suurim_skoor = riigi_skoor
            voitja = riigi_nimi
print(f"Võitja on {voitja} kogusummaga {suurim_skoor} punkti")
    
    