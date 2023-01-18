failinimi = input("Sisesta andmefaili nimi: ")
vaatluskoht = input("Sisesta vaatluskoht: ")
liike_vaatluskohas = 0
linde_vaatluskohas = 0
liike_kokku = 0
linde_kokku = 0
print(f"Linde vaatluskohas '{vaatluskoht}':")

with open(failinimi, encoding = "UTF-8") as fail:
    while True:
        lind = fail.readline().strip()
        if lind == "":
            break
        koht = fail.readline().strip()
        arv = int(fail.readline().strip())
        linde_kokku += arv
        liike_kokku += 1
        if koht == vaatluskoht:
            linde_vaatluskohas += arv
            liike_vaatluskohas += 1
            print(f"{lind}: {arv} ")
            
if linde_vaatluskohas > 0:
    print(f"Vaatluskohas oli kokku {linde_vaatluskohas} lindu ja {liike_vaatluskohas} linnuliiki.")
    print(f"Vaatluskohas vaadeldi {round(linde_vaatluskohas/linde_kokku*100, 2)}% kõikidest lindudest.")
else:
    print("Sellist vaatluskohta ei ole.")

with open("vaadeldud.txt", "w", encoding = "UTF-8") as g:
    g.write(f"Kokku vaadeldi {linde_kokku} lindu.\n")
    g.write(f"Leiti {liike_kokku} linnuliiki.\n")
    if liike_vaatluskohas > 1:
        g.write(f"Vaatluskohas '{vaatluskoht}' vaadeldi {liike_vaatluskohas} linnuliiki.")
