def sugavus(vaartus):
    if type(vaartus) != list:
        return 0
    
    maksimaalne_sugavus = 0
    for el in vaartus:
        el_sugavus = sugavus(el)
        if el_sugavus > maksimaalne_sugavus:
            maksimaalne_sugavus = el_sugavus
    return maksimaalne_sugavus + 1

print(sugavus([1, 2,[2, [2]]]))