faili_nimi = input("Sisesta faili nimi: ")
vaatluskoht = input("Siseta vaatlus koht: ")


fail = open(faili_nimi, "r")
read_fail = fail.readlines()

koik_linnud = 0
for i in range(2, len(read_fail), 3):
    koik_linnud += int(read_fail[i])

koik_liigid = 0
for i in range(0, len(read_fail), 3):
    koik_liigid += 1

if vaatluskoht in "".join(read_fail):
    kokku_lindu = 0
    kokku_liiki = 0
    print(f"Linde vaatluskohas '{vaatluskoht}':")
    for i in range(0, len(read_fail)):
        if vaatluskoht in read_fail[i].split():
            kokku_lindu += int(read_fail[i + 1].strip())
            kokku_liiki += 1
            print(read_fail[i - 1].strip() + ":", read_fail[i + 1].strip())
            
   

    print(f"Vaatluskohas oli kokku {kokku_lindu} lindu ja {kokku_liiki} linnuliiki.\nVaatluskohas vaadeldi {round(kokku_lindu/koik_linnud*100,2)}% kokidest lindudest.")

    
        

    uus_fail = open("vaadeldud.txt", "w")
    uus_fail.write(f"Kokku vaadeldi {koik_linnud} lindu.\nLeiti {koik_liigid} linnuliiki.\nVaatluskohas '{vaatluskoht}' vaadeldi {kokku_liiki} linnuliiki.")

else:
    print(f"Linde vaatluskohas '{vaatluskoht}':\nSellist vaatluskohta ei leidu")
    uus_fail = open("vaadeldud.txt", "w")
    uus_fail.write(f"Kokku vaadeldi {koik_linnud} lindu.\nLeiti {koik_liigid} linnuliiki.")


fail.close()
uus_fail.close()