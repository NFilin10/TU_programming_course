n = int(input("Sisesta n: "))
korr = 1
for i in range(1, n+1):
    korr *= (2 * i) / (2 * i - 1) * (2 * i) / (2 * i + 1)
    
print("Korrutis on", korr * 2)
    