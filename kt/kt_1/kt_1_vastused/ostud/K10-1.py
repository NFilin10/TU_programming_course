fail = input('Sisesta failinimi: ')
mitte_osta = input('Mida poest mitte osta: ')
ostetud_esemed = ''
summa = 0

with open(fail, 'r', encoding='UTF-8') as f:
    while True:
        nimi = f.readline().strip()
        if nimi == '':
            break
        hind = float(f.readline())
        kogus = int(f.readline())        
        if nimi == mitte_osta:
            continue        
        summa += hind * kogus        
        ostetud_esemed += nimi + ' '
        
print('Ostunimekiri:', ostetud_esemed)
print('Ostu maksumus on', summa, 'eurot.')

with open('raha.txt', 'w', encoding='UTF-8') as g:
    if summa <= 15:
        print('Pillel jätkus raha poes käimiseks!')
        g.write(f'Pillel jäi raha üle {round(15 - summa, 2)} eurot.')
    else:
        print('Pillel ei jätkunud raha poes käimiseks')
        g.write(f'Pillel jäi raha puudu {round(summa - 15, 2)} eurot.')   
