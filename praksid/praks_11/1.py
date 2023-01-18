
def esineb(otsitav, jrj, mitu):
    if not jrj:
        return False
    if jrj[0] == otsitav:
        if mitu == 1:
            return True
        else:
            mitu -= 1
    return esineb(otsitav, jrj[1:], mitu)

print(esineb("a", ['a', 'g'], 1))