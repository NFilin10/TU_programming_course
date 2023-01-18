from time import time

välgusähvatus = input("Vajuta Enter, kui nägid välgusähvatust ")
aeg_1 = time()

kõmin = input("Vajuta Enter, kui nägid kõminat ")
aeg_2 = time()

aega_kulunud = aeg_2 - aeg_1

kaugus = aega_kulunud * 343
print("Äike oli", kaugus, "meetri kaugusel")