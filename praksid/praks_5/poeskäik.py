fail = open("test.txt")

sum = 0
kaup = 0
for i in fail.readlines():
    try:
        sum += float(i)
        kaup += 1
    except :
        pass
print(f"Ostetud kaupade koguarv on {kaup}, kogusummaga {sum}.")
fail.close()