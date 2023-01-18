def on_järjestatud(jrj):
    for i in range(len(jrj)-1):
        if jrj[i].lower() > jrj[i+1].lower():
            return False
    return True 

def on_vaiksem(a, b):
    return a.lower() < b.lower()
    

def loe_sonad(failinimi):
    inglise_sonad = []
    eesti_sonad = []
    
    with open(failinimi) as fail:
        for rida in fail.read().strip().split('\n'):
            eng_est = rida.split()
            inglise_sonad.append(eng_est[0])
            eesti_sonad.append(eng_est[1])
            
    print(on_järjestatud(inglise_sonad))
    return inglise_sonad, eesti_sonad

def leia_vaste(inglise_sonad, eesti_sonad, algus, lopp, sona):
    while algus != lopp:
        keskpunkt = (algus+lopp)//2
        if on_vaiksem(inglise_sonad[keskpunkt], sona):
            algus = keskpunkt
        else:
            lopp = keskpunkt
            
    return eesti_sonad[algus]
        
    
    
inglise_sonad, eesti_sonad = loe_sonad("sonastik.txt")

sona = input("Sisesta inglisekeelne sona: ")
print("Eesti keelne vaste: "+leia_vaste(inglise_sonad, eesti_sonad, 0, len(inglise_sonad), sona))