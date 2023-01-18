def võitja(m):
    cX = 0
    cO = 0
    
    tulemus = {}
    
    #read
    for i in range(0, len(m)):
        for j in range(0, 2):
            if m[i][j] == m[i][j+1] == m[i][j+2] == "X":
                cX += 1
            elif m[i][j] == m[i][j+1] == m[i][j+2] == "O":
                cO += 1
                
    #veerud
    for i in range(0, 2):
        for j in range(0, len(m)):
            if m[i][j] == m[i+1][j] == m[i+2][j] == "X":
                cX += 1
            elif m[i][j] == m[i+1][j] == m[i+2][j] == "O":
                cO += 1
    
    #diagonal1
    for i in range(0, 2):
        for j in range(0, 2):
            if m[i][j] == m[i+1][j+1] == m[i+2][j+2] == "X":
                cX += 1
            elif m[i][j] == m[i+1][j+1] == m[i+2][j+2] == "O":
                cO += 1
                
    #diagonal2
    for i in range(0, 2):
        for j in range(0, 2):
            if m[i+2][j] == m[i+1][j+1] == m[i][j+2] == "X":
                cX += 1
            elif m[i+2][j] == m[i+1][j+1] == m[i][j+2] == "O":
                cO += 1
    
    tulemus["O"] = cO
    tulemus["X"] = cX
    
    return tulemus

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))