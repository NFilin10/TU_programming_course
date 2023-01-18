
with open('sünnid.txt') as fail:
    synnid = fail.read().strip().split("\n")
    
with open('surmad.txt') as fail:
    surmad = fail.read().strip().split("\n")
    

print("Positiivse iibega kuud olid:")

kokku = 0
for i in range(len(surmad)//2):
    kuu = surmad[i*2]
    iive = int(synnid[i*2+1])-int(surmad[i*2+1])
    kokku += iive
    
    if iive > 0:
        print(kuu, iive)
        
print(f"Kogu ajavahemiku loomulik iive oli {kokku}.")