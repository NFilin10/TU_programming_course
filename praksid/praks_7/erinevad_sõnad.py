
def erinevad_sonad(s):
    erinevad = []
    esimisagedused = []
    
    jrj = s.lower().split()
    
    for sona in jrj:
        sona = sona.strip('.!?,')
        
        if sona not in erinevad:
            erinevad.append(sona)
            esimisagedused.append(1)
            
        else:
            esimisagedused[erinevad.index(sona)] += 1
        
    return erinevad, esimisagedused

print(erinevad_sonad("tere Tere tore"))