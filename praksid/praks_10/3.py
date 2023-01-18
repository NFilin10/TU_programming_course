def valuutavahetus(sonastik):
    sonastik["EUR"] = 1
    tulemus = {}
    
    for valuuta1 in sonastik:
        for valuuta2 in sonastik:
            if valuuta1 != valuuta2:
                if valuuta1 not in tulemus:
                    tulemus[valuuta1] = {}
                    
                tulemus[valuuta1][valuuta2] = round(sonastik[valuuta2]/sonastik[valuuta1], 4)
    return tulemus
    
    
    
    
print(valuutavahetus({'USD': 0.9993, 'GBP': 0.8714, 'PLN': 4.6865}))