from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(tähis, arg):
    if tähis == "K":
        if loetleFilmid(arg[0]) == []:
            print("sellist zanri ei ole, palun proovige uuestu")
        print("Võimalikud filmid on:")
        for i in loetleFilmid(arg[0]):
            print(i)
        
        return True
    
    elif tähis == "L":
        if len(arg) > 2:
            arg_len = len(arg) - 1
            lisaFilm(str(arg[1])+" "+str(arg[arg_len]), arg[0])
            return True
        lisaFilm("".join(arg[1]), arg[0])
        print("Film lisatud!")
        return True
        
    elif tähis == "V":
        print("".join(arg[0]))
        kustutaFilm(" ".join(arg))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    
    elif tähis == "E":
        return False
 
while True:
    print('''=== FILMIANDMEBAAS ===
    Kuva filmid: K <žanr>
    Lisa film:   L <žanr> <film>
    Vaata filmi: V <filmi nimi>
    Lõpeta:      E
    ===
    ''')

    user_input = input("Vali käsk: ")
    tähis = user_input[0]
    arg = list(user_input[1:].split())
    if töötleKäsk(tähis, arg) == False:
        break

