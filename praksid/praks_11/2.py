

def kolmeaastane(vastus):
    if vastus == "midagi":
        return
    else:
        vastus = input("Aga miks? ")
    kolmeaastane(vastus)
    
vastus = input("Miks on taevas sinine? ")
kolmeaastane(vastus)