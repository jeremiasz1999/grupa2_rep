moje_piwo = ['rzeski', 'jasny', 'lekki']

lager = ['rzeski', 'jasny', 'lekki']
pils = ['jasny', 'goryczkowy', 'średnio-mocny']
porter = ['gorzki', 'mocny', 'ciemny']
stout = ['ciemny', 'kawowy', 'bogaty']
bezalkoholwe = ['owocowe', 'lekkie', 'bezalkoholwe']
ale = ['lekki', 'owocowy', 'kwiatowy']

wybrane_piwa = []
piwa = [lager, pils, porter, stout, bezalkoholwe, ale]

if moje_piwo == lager:
    wybrane_piwa.append('lager')
if moje_piwo == pils:
    wybrane_piwa.append('pils')
if moje_piwo == porter:
    wybrane_piwa.append('porter')
if moje_piwo == stout:
    wybrane_piwa.append('stout')
if moje_piwo == bezalkoholwe:
    wybrane_piwa.append('bezalkoholowe')
if moje_piwo == ale:
    wybrane_piwa.append('ale')

print(wybrane_piwa)
