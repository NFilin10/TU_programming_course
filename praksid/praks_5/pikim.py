fail = open("lemmad.txt")
lemmad = fail.read().strip().split("\n")

def unukaalsed(s):
    s2 = ''
    
    for tht in s:
        if tht in s2:
            return False
    
        s2+=tht
    return True

pikim = ''

for lemma in lemmad:
    if unukaalsed(lemma) and len(lemma) > len(pikim):
        pikim = lemma
print(pikim)
    