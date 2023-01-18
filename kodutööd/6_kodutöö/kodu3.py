#34501234215
#23. jaanuar 1945'


def sünnikuupäev(id):
    kuupaev = id[5:7]
    if id[0] == "1" or id[0] == "2":
        aasta = "18" + id[1:3]
    elif id[0] == "3" or id[0] == "4":
        aasta = "19" + id[1:3]
    elif id[0] == "5" or id[0] == "6":
        aasta = "20" + id[1:3]
        
    kuu_num = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuu_num[int(id[3:5])-1]
    return f"{kuupaev}. {kuu} {aasta}"

print(sünnikuupäev("50308050851"))