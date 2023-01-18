
def loetleFilmid(zanr):
    file = open("filmid.txt", "r")
    read_file = file.read().strip().split("\n")

    formatted_list = []
    filmid = []
    file.close()

    for i in read_file:
        formatted_list.append(i.split(" - "))
    for i in formatted_list:
        if zanr in i:
            filmid.append(i[0])

    file.close()

    return filmid


def lisaFilm(nimi, zanr):
    file = open("filmid.txt", "a")
    file.write("\n" + nimi + " - " + zanr + "\n")

    file.close()


def kustutaFilm(nimi):
    file = open("filmid.txt", "r+")
    read_file = file.read().strip().split("\n")

    for i in read_file:
        if nimi in i:
            read_file.remove(i)

    file = open("filmid.txt", "w")

    for i in read_file:
        file.write(i + "\n")

    file.close()


