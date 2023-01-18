def poisse_ja_tüdrukuid(sugu):
    poisid = 0
    tudrukud = 0
    for  i in sugu:
        if i[-1] == "P":
            poisid += 1
        else:
            tudrukud += 1
    return poisid, tudrukud
    
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))