def arvuta_tasu(tunnid, tasu):
    if tunnid <= 40:
        return tunnid * tasu
    return 40 * tasu + 1.5 * (tunnid - 40) * tasu

nimi_1 = str(input("Sisetsa töötaja nimi: "))
tunnid_1 = float(input("Sisesta töötaja tunnid: "))
tasu_1 = float(input("Sisesta töötaja tasumäär: "))
tulu_1 = arvuta_tasu(tunnid_1, tasu_1)

nimi_2 = str(input("Sisetsa töötaja nimi: "))
tunnid_2 = float(input("Sisesta töötaja tunnid: "))
tasu_2 = float(input("Sisesta töötaja tasumäär: "))
tulu_2 = arvuta_tasu(tunnid_2, tasu_2)

if tulu_1 > tulu_2:
    print(nimi_1, "saab suuremat tasu kui", nimi_2)
    
elif  tulu_1 < tulu_2:
    print(nimi_2, "saab suuremat tasu kui", nimi_1)

