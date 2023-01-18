lohed = int(input("Sisesta lohede arv: "))
maod = int(input("Sisesta madude arv: "))
saurused  = int(input("Sisesta sauruste arv: "))
paevad = 1

while True:
    söömisi_lohed = min(lohed, maod)
    maod -= söömisi_lohed
    
    söömisi_maod = min(maod, saurused)
    saurused -= söömisi_maod
    
    söömisi_saurused = min(saurused, lohed)
    lohed -= söömisi_saurused
    
    söömisi = söömisi_lohed + söömisi_maod + söömisi_saurused
    
    if söömisi > 0:
        pass
    else:
        break
    paevad += 1
print("Viimane söögikord oli", paevad-1)
if maod > 0:
    print("Järele jäi", maod, "madu")
elif lohed > 0:
    print("Järele jäi", lohed, "lohet")
elif saurused > 0:
    print("Järele jäi", saurused, "saurust")





    