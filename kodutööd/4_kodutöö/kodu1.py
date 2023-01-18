arv = int(input("Sisesta arv: "))
sammud = 0

while arv != 1:
    if arv % 2 == 0:
        arv = arv / 2
        sammud += 1
    else:
        arv = arv * 3 + 1
        sammud += 1
print("Sammude arv on " + str(sammud) + ".")

