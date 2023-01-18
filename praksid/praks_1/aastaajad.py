kuu = int(input("Sisesta kuu number: "))

if kuu == 12 or kuu == 1 or kuu == 2:
    print("talv")
    
elif kuu >= 3 and kuu <= 5:
    print("kevad")

elif kuu >= 6 and kuu <= 8:
    print("suvi")

elif kuu >= 9 and kuu <= 11:
    print("sügis")
    
else:
    print("Kontrolli kuu number")
