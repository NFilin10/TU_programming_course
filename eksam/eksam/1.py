def püramiid(kiht):
    if kiht == 1:
        return 1
    else:
        return püramiid(kiht-1) + (kiht)

print(püramiid(5))