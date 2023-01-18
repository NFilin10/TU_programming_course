

def failist_järjendisse(f):
    f = open(f)

    bingo = []

    for line in f.readlines():
        bingo.append(line.strip().split(" "))
        
    for i in range(0, len(bingo)):
        for y in range(0, len(bingo[i])):
            bingo[i][y] = int(bingo[i][y])
    
    f.close()
    return(bingo)


def on_bingo_tabel(m):
    
    index = 0
    rule_min = 1
    rule_max = 15
    
    for i in range(0, 5):
        for veerg in m:
            if rule_min <= veerg[i] <= rule_max:
                pass
            else:
                return False
            
        rule_min = rule_max
        rule_max += 15
  
    return True

   
print(on_bingo_tabel([[1, 30, 34, 55, 75],
                    [10, 16, 40, 50, 67],
                    [5, 20, 38, 48, 61],
                    [4, 26, 43, 49, 70],
                    [15, 17, 33, 51, 66]]))
        
