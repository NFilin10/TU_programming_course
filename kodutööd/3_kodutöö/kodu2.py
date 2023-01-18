def summa(u, v):
    c = 299792458 / 1000
    return (u + v) / (1 + (u * v) / c ** 2)

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
uv = summa(u, v)

x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
uvx = summa(uv, x)

y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
uvxy = summa(uvx, y)

print("Kiiruse summa on", uvxy, "km/s")