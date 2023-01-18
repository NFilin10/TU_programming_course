import os.path

def faili_suurus(fail):
    if os.path.exists(fail) and not os.path.isdir(fail):
        return os.path.getsize(fail)
    if os.path.isdir(fail):
        print("Tegu on kaustaga")
    else:
        return 0
    
    
def teisenda(baidid):
    if baidid < 512:
        return str(round(baidid), 2) + " B"
    
    baidid = baidid / 1024
    
    if baidid < 512:
        return str(round(baidid, 2)) + " KB"
    
    baidid = baidid / 1024
    
    if baidid < 512:
        return str(round(baidid, 2)) + " MB"
    
    baidid = baidid / 1024

    return str(round(baidid, 2)) + " GB"


def suuruse_leidja(fail):
    return teisenda(faili_suurus(fail))

fail = input("Sisesta faili nimi: ")

print("Faili suurus on: ", suuruse_leidja(fail))
