aasta = int(input("Sisestage aasta: "))

a = aasta % 19
b = aasta // 100
c = aasta % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
j = c % 4
k = (32 + 2 * e + 2 * i - h - j) % 7
l = (a + 11 * h + 22 * k) // 451
m = (h + k - 7 * l + 114) // 31
n = (h + k - 7 * l + 114) % 31

kuu = m
paev = n + 1

print(paev, "-", kuu, "-", aasta)