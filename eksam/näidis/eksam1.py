def kilekotte(poes_kaik):
    if poes_kaik == 1:
        return 2
    elif poes_kaik == 0:
        return 0
    elif poes_kaik % 3 == 1:
        return kilekotte(poes_kaik-1)+2
    else:
        return kilekotte(poes_kaik-1)+1

print(kilekotte(7))