def seosta_lapsed_ja_vanemad(lapsed, nimed):
    with open(lapsed) as fail:
        lapsed = fail.read().strip().split("\n")
    with open(nimed) as fail:
        nimed = fail.read().strip().split("\n")
        
    nimi_kood_dict = {}
    for nimi_kood in nimed:
        nimi, kood = nimi_kood.split(" ", 1)
        nimi_kood_dict[nimi] = kood
    vanem_laps_dict = {}
    
    for vanem_laps in lapsed:
        vanem_id, laps_id = vanem_laps.split()
        if laps_id not in vanem_laps_dict:
            vanem_laps_dict[laps_id] = set()
            vanem_laps_dict[laps_id].add(vanem_id)
        else:
            vanem_laps_dict[laps_id].add(vanem_id)
    
    result = {}
    
    for laps, vanem in vanem_laps_dict.items():
        vanemad = set()
        for v in vanem:
            vanemad.add(nimi_kood_dict[v])
        result[nimi_kood_dict[laps]] = vanemad
    
    for laps, vanemad in result.items():
        print(f"{laps}: {', '.join(vanemad)}")
    return result
    
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")