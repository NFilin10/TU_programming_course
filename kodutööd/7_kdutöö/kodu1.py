from random import sample

def bingo():
    arvude_list = []
    esimesed_kolm = sample(range(1, 11), 3)
    if 1 in esimesed_kolm and 2 in esimesed_kolm and 3 in esimesed_kolm:
        esimesed_kolm = sample(range(1, 11), 3)
    teised_kaks = sample(range(11, 21), 2)
    return esimesed_kolm + teised_kaks

print(bingo())