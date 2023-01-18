def teisenda(R, G, B):
    x_min = min(R, G, B)
    x_max = max(R, G, B)
    
    L = (x_min + x_max) / 2
    
    if x_min == x_max:
        H = 0
        S = 0
    
    else:
        if x_max == R:
            H = (G - B) / (x_max - x_min)
        elif x_max == G:
            H = 2 + (B - R) / (x_max - x_min)
        else:
            H = 4 + (R - G) / (x_max - x_min)
            
        if H < 0:
            H = H + 6
        
        H = H * 60
        
        if L < 0.5:
            S = (x_max - x_min) / (x_max + x_min)
        else:
            S = (x_max - x_min) / (2 - x_max - x_min)
            
    return H, S, L
        
print(teisenda(0.1, 0.3, 0.9))