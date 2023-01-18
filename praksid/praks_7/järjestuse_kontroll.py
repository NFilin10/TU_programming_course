def on_järjestatud(jrj):
    for i in range(len(jrj)-1):
        if jrj[i] > jrj[i+1]:
            return False
    return True 

print(on_järjestatud([1, 2, 3]))