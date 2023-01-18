def päevade_arv(kuu):

    paevad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= int(kuu) <= 12:
        return paevad[kuu-1] 
    else:
        return -1

while True:
    try:
        kuu = input("Sisesta kuu number: ")
        if 1 <= int(kuu) <= 12:
            print("Selles kuus on", päevade_arv(int(kuu)), "päeva")
        else:
            print("Kuu number peab jääma lõiku 1–12")
        
    except:
        if not kuu:
            break
        else:
            print("Ebakorrektne number")
    

    