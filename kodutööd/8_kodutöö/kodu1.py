
def failist_järjendisse(f):
    
    f = open(f)

    retseptid = []

    for line in f.readlines():
        retseptid.append(line.strip().split(","))
       
    f.close()
    return retseptid
    
print("Retseptid, milleks on vaja maasikaid ja suhkrut:")

for el in failist_järjendisse("retseptid.txt"):
    if "suhkur" in el and "maasikad" in el:
         print(",".join(el))


