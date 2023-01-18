fail = input("Sisesta faili nimi: ")

with open(fail) as f:
    sisu = f.read().strip().split("\n")
    
jrj = []
dic = {}

for i in sisu:
    klassid = i.split(" ")[0]
    kohad = i.split(" ")[1]
    jrj.append(i.split())
    dic[klassid] = len(kohad)
    
klass = input("Mis klassist olete? ")
pileteid = input("Mitu piletit soovite? ")


def kontrolli_kohad(klass, pileteid, jrj):
    esialgu = pileteid
    koik_kohad = []
    koht = []
    rida = []
    pileteid = int(pileteid) -1
    
    for i in jrj:
        if i[0] == klass:
            kokku = "-" * (pileteid+1)
            
            for j in range(0, len(i[1])):
                pileteid += 1
                if i[1][j:pileteid] == kokku:
                    for s in range(j, pileteid):
                        koik_kohad.append(f"(rida {jrj.index(i)+1}, koht {s+1})")
                        koht.append(s)
                        rida.append(jrj.index(i))
                break
            pileteid = int(esialgu) - 1
            
    return koik_kohad, koht, rida, pileteid

def muuda(rida, pileteid):
    rida = rida[0:len(rida):2]
    with open(fail, "r") as f:
        d = f.read()
        c = d.strip().split("\n")
        
        for i in rida:
            r = c[i].split(" ")[1]
            print(r)
            a = r.replace("-"*int(pileteid), "x"*int(pileteid), 1)
            data = d.replace(r,a)

            with open(fail, "w") as o:
                o.write(data)
    
if kontrolli_kohad(klass, pileteid, jrj)[0] == []:
    print("Viga")
    
else:
    print(f"Teie kohad on {', '.join(kontrolli_kohad(klass, pileteid, jrj)[0])}")
    muuda(kontrolli_kohad(klass, pileteid, jrj)[2], pileteid)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    