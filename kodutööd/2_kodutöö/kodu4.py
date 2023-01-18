aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu < 6000:
    print("Maksuvaba tulu on", round(aastatulu, 2), "eurot")
elif 6000 <= aastatulu < 14400:
    print("Maksuvaba tulu on 6000 eurot")
elif 14400 <= aastatulu < 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print("Maksuvaba tulun on", round(maksuvaba_tulu, 2), "eurot")
elif aastatulu >= 25200:
    print("Maksuvaba tulun on 0 eurot")