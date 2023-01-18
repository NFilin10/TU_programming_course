def loe_sisse(failinimi):
    with open(failinimi) as fail:
        read = fail.read().strip().split("\n")
        
    jrj = []
    
    for rida in read:
        sonastik = {}
        rida = rida.split(";")
        
        for vaartus in rida:
            voti_vaartus = vaartus.split("=")
            sonastik[voti_vaartus[0]] =  voti_vaartus[1]
        jrj.append(sonastik)
    return jrj
    
    
def kirjuta_faili(jrj, failinimi):
    sisu = ""
    for sonastik in jrj:
        rida = []
        for voti in sonastik:
            rida.append(voti+"="+sonastik[voti])
        rida = ";".join(rida)
        sisu += rida+"\n"
 

    with open(failinimi, "w") as fail:
        fail.write(sisu)

jrj = loe_sisse("kontaktid.txt")

for sonastik in jrj:
    while True :
        print(sonastik)
        voti = input("Sisesta millist valja tahad lisada, lopetamisesk vajuta enterit: ")
        
        if voti == "":
            break
        
        vaartus= input("Sisesta valja vaartus: ")
        
        sonastik[voti] = vaartus
        
kirjuta_faili(jrj, "kontaktid.txt")
        
