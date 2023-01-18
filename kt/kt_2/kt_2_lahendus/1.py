def loe_autod(failinimi):
    with open(failinimi) as fail:
        sisu = fail.read().strip().split("\n")
    
    s = {}
    for auto in sisu:
        info = auto.split(";")
        info[1] = int(info[1])
        s[info[0]] = info[1:4]
    return s
     
print(loe_autod("autod.txt"))

def autode_hinnad(s):
    uus_s = {}
    for k, v in s.items():
        v[0], v[1] = v[1], v[0]
        uus_s[tuple(v)] = k
    return uus_s


print(autode_hinnad(loe_autod("autod.txt")))


autode_sonastik = loe_autod("autod.txt")
max_hind = int(input("Sisesta auto maksimaalne hind: "))
mark = input("Sisesta auto mark: ")

sobivaid = 0
for info, number in autode_hinnad(autode_sonastik).items():
    if mark in info and info[1] <= max_hind:
        print(number, info[0], info[1], info[2])
        sobivaid +=1
if sobivaid == 0:
    print("Ei ole sobivat autot.")

    

