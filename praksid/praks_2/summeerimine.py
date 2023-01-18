f = open("test.txt")
sisu = f.read().strip()
read = sisu.split("\n")

summa = 0

for rida in read:
    summa = summa + (int(rida))
    
print(summa)

f.close()