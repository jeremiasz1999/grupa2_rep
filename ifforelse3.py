piwa = {

"Tyskie": (5.6, 4.5),

"Żywiec Porter": (9.5, 8.0),

'Lech': (5.2, 4.0),

"Perła Chmielowa": (6.2, 3.8),

'Warka Silna': (6,5, 5,5),

"Żubr": (6.0, 4.0),

"Kombinezon": (7.0, 2.5),

'Komes Porter': (9,0, 10,0),

"Żywiec Białe": (5.0, 5.0),

"Okocim Mocne": (7.0, 3.5),

'Desperaci': (5.9, 6.0),

'Somersby': (4,5, 5,0),

"Harnaś": (6.0, 3.0),

}

lista_piw = list(piwa.keys())
lista_piww = []
wybrane = []
i=None
j= None

# for i in lista_piw:
#     for j in piwa[i].items():
#         lista_piww.append(j)
#

nazwa = None
moc = None
cena = None
for nazwa, parametry in piwa.items():
    for i in parametry:
        lista_piww.append(i)
for j in lista_piww[0::2]:
        if j >= 6:
            print(f'{nazwa}')