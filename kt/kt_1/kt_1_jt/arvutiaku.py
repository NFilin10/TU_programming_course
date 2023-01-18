def aku_aeg(akumaht, vanus):
    if vanus > 3:
        return round(akumaht/15*60)
    else:
        return round(akumaht/8*60)


def kas_akust_piisab(eeldatav_aeg, kasutamise_aeg):
    if eeldatav_aeg > kasutamise_aeg:
        return True
    else:
        return round(kasutamise_aeg - eeldatav_aeg)


akumaht = int(input("Sisesta arvuti akumahu näit protsentides? "))
kestvus = int(input("Kui kaua soovid arvutit veel kasutada? "))
vanus = int(input("Kui vana on arvuti aku? "))


if kas_akust_piisab(aku_aeg(akumaht, vanus), kestvus) != True:
    print(f"Puudu jääb {kas_akust_piisab(aku_aeg(akumaht, vanus), kestvus)} minutit. Arvuti tuleb laadima panna.")

else:
    print(f"Arvuti akumahust piisab vähemalt {kestvus} minutiks.")
