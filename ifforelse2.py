puby = {
    'Pub1': ['zywiec', 'perla', 'konska dawka'],
    'Pub2': ['gaska  beerbika', 'specjal'],
    'Pub3': ['balios', 'orkiszowe', 'ucho od sledzia'],
    'Pub4': ['zywiec', 'fabrykanckie swinie']
}
lista_pub = list(puby.keys())
moje_piwo = 'ucho od sledzia'

i = 0
# while moje_piwo != _:
for i in lista_pub:
    if moje_piwo in puby[i]:
        print(f'{i}')
    else:
        pass



