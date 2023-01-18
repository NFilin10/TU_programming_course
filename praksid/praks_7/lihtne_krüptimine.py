
def krüpti_sõne(sonum, nihe):
    tahestik = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    
    krupteeritud = ""
    
    for taht in sonum:
        indeks = tahestik.index(taht)
        nihutatud_indeks = indeks + nihe
        krupteeritud += tahestik[nihutatud_indeks % 27]
        
    return krupteeritud

print(krüpti_sõne("PALUN TULE SIIA", 5))
        
    