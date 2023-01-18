temp = int(input("Mis temperatuur väljas on? "))
päike = str(input("Kas päike paistab? "))
lipp = str(input("kas rannas lehvib roheline lipp? "))

if temp >= 20 and päike == "jah" or lipp == "jah":
    print("Võid minna randa!")

else:
    print("Täna ei tasu randa minna.")
