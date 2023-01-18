def kirja_hind(kaal):
    if kaal <= 250:
        return 1.75
    elif kaal <= 500:
        return 2.70
    elif kaal <= 1000:
        return 2.85
    else:
        return 4.35

kirjade_arv = int(input("Sisesta kirjade arv: "))
summa = 0
kirja_nr = 1

while kirja_nr <= kirjade_arv:
        kaal = int(input("Sisesta "+ str(kirja_nr) + ". kirja kaal: "))
        summa += kirja_hind(kaal)
        kirja_nr += 1
print("Nende kirjade saatmine läheb maksma", summa, "eurot.")