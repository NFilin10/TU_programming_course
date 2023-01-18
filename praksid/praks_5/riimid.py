
def RN(s1, s2):
    min_pikkus = min(len(s1), len(s1))
    
    riimumisnaiteja = 0
    
    for i in range(-1, -1*min_pikkus-1, -1):
        if s1[i] == s2[i]:
            riimumisnaiteja += 1
        else:
            break
    return riimumisnaiteja

        

fail = open("lemmad.txt")
lemmad = fail.read().strip().split("\n")

sona = input("Sisesta algne sõna: ")
min_rn = int(input("Sisesta minimaalne riimumisnaitaja: "))

for lemma in lemmad:
    if RN(lemma, sona) >= min_rn:
        print(lemma)

fail.close()