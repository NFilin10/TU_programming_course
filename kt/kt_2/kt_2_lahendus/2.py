def loe_info(failinimi):
    with open(failinimi) as fail:
        sisu = fail.read().strip().split("\n")
    andmed = []
    
    for rida in sisu:
        info = rida.split(";")
        andmed.append(info)
    for i in andmed:
        i.pop(1)


    for i in andmed:
        for j in range(1, 6):
            i[j] = int(i[j])
            i[-1] = float(i[-1])
    return andmed

        
    

            
        
    

print(loe_info("lauluvõistlus.txt"))