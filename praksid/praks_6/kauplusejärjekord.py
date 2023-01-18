esemed = input("Sisesta esemete arvud: ")

esemete_list = esemed.split()

kokku = len(esemete_list)

print(f"Järjekorras seisab {kokku} inimest")
  

counter = 0
jrj_nr = 1
suurim_esemete_arv = 0
suurim_jr_nr = 1
for i in esemete_list:
    i = int(i)
    if i > 3:
        counter += 1
    if i > suurim_esemete_arv:
        suurim_esemete_arv = i
        suurim_jr_nr = jrj_nr
    jrj_nr += 1
print(f"Rohkem kui kolm eset on korvis {counter} inimesel")
print(f"Kõige rohkem esemeid on {suurim_jr_nr}. inimesel, kellel on {suurim_esemete_arv} eset")