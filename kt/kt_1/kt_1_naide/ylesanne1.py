f = open("hinnad.txt", "r")

new_f = open("uued_hinnad.txt", "w")

read_f = f.readlines()

for i in range(0, len(read_f), 2):
    try:
        if int(read_f[i+1]):
            print(f"{read_f[i].strip()} OK!")
            new_f.write(read_f[i])
            teisenda = float(read_f[i+1]) - 0.01
            new_f.write(str(teisenda) + "\n")
    except:
        print(f"Toote '{read_f[i].strip()}' hinda '{read_f[i+1].strip()}' ei õnnestunud teisendada.")

f.close()
new_f.close()
            