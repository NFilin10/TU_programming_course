with open("a.txt") as fail:
    read1 = fail.read().strip().split("\n")
    
with open("b.txt") as fail:
    read2 = fail.read().strip().split("\n")
    
with open("c.txt", "w+") as fail:
    for i in range(len(read2)):
        indeks = int(read2[i]) - 1
        voistelja = read1[indeks]
        nimi = voistelja.split()[1]
        fail.write(str(i+1)+". " + nimi + "\n")    
    
