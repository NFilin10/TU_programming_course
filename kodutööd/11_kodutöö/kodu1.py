def auto_hind(hind, aasta):
    if aasta <= 0:
        return round(hind, 2)
    else:
        return auto_hind(round(hind-hind*0.2, 2), aasta-1)

print(auto_hind(10000, 5))