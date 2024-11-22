# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # **Typowanie zmiennych w Pythonie**

# %% [markdown]
# ## Typy zmiennych

# %% [markdown]
# Lista typów:

# %%
list = [1, 10.0, True, "test", b"test", {1, "2"}]
for _ in list:
    print(type(_))

# %%
print(type(x))

# %%
max({"1", "ryev"})

# %%
max({1, 5, 8, "1"})

# %%
x: tuple[int, str, float] = (3, "text", 7.5)
x[0]

# %%
x: dict[int, str, float] = {"jeden": 3, "dwa": "text","trzy": 7.5}
x["dwa"]

# %% [markdown]
# ## Typowanie statyczne

# %% [markdown]
# ## Typowanie dynamiczne

# %% [markdown]
# ## Dodawanie typów zmiennych do funkcji

# %%
import mypy as mp

# %%
"""Dodawanie Type Hints do funkcji"""

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


# %%
print(headline("python type checking"))

# %%
print(headline("python type checking", align=False))

# %%
print(headline("python type checking", align="center"))

# %%
# ! mypy headlines.py

# %%
"""Ponownie wykorzystujemy funckje headline, ale teraz deklarujemy domyślną wartość drugiej zmiennej jako False"""

def headline_2(text, centred: bool = False) -> str:
    if not centred:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


# %%
print(headline_2("python type checking", centred=True))

# %%

# %% [markdown]
# ## Wady i zalety typowania zmiennych

# %% [markdown]
# Zalety typowania zmiennych:
# - Dokumnetacja kodu pozwala innym użytkowanikom poprawnie odczytać kod.
# - Dzięki typowaniu zmiennych nasz interpreter jest w stanie udzielać nam podpowiedzi.
# - Pozowala utrzymać czystość kodu, przy częstym stosowaniu duck typing łatwo się pogubić.

# %% [markdown]
# Wady typowania zmiennych: 
# - Wymaga więcej czasu podczas pisania kodu, z drugiej strony prawdopodobnie poświęcimy mniej czasu na szukaniu błędów.
# - Adnotacje do funkcji czy danych są stosunkowo nowym sposobem na typowanie danych i zostały wprowadzone od pythona 3.0.
# - Typowanie może sprawić że skrypt będzie się dłużej uruchamiał (dotyczy to szczególnie tych krótkich).

# %% [markdown]
# Nie ma jednoznacznej dopowiedzi kiedy powinniśmy używać typowania danych. Na pewno nie należy popadać w żadną skrajność. Warto skupić się
# na najważenijszych częściach kodu i odpowiednio go opisać.

# %% [markdown]
# ## Type Annotations or Type comments

# %% [markdown]
# Adnotacje służą do opisu argumentów funkcji oraz wartości, które ma zwrócić: 

# %%
# def func(arg: arg_type, optarg: arg_type = default) -> return_type:

# %% [markdown]
# Argumenty funkcji opisujemy następująco argument: adnotacja typu. Typ wartości, którą zwróci -> adnotacja. Typy danych,
# które można wyróżnić zostały opisane w 1 rozdziale.

# %%
import math

"""Funkcja liczy obwód koła"""

def circumference(radius: float) -> float:
    return 2 * math.pi * radius

print(circumference(4))

# %%
circumference.__annotations__

# %%
circumference(4)


# %%
# ! mypy circumference.py

# %%
def reveal_type(x):
    return type(x)
    
print(reveal_type("tekst"))

# %%
# """zmienne bez adnotacji"""

# import math

# reveal_type(math.pi)

# radius = 1
# circumference = 2 * math.pi * radius
# reveal_locals()

# %%
# ! mypy reveal.py

# %% [markdown]
# Jak widać powyżej mypy odczytał typy zmiennych bez adnotacji.

# %%
pi: int = 3.142

def circumference(radius: float) -> float:
    return 2 * pi * radius


# %%
circumference.__annotations__

# %%
__annotations__

# %%
# !mypy circumference2.py

# %% [markdown]
# Teraz dodajemy adnotacje do zmiennej występującej funkcji. Atrybut funkcji: circumference.__annotations\_\_ nie przechowuje informacji o typie tych zmiennych, ale mypy jest w stanie wykryć że nie zgadzają się typy danych. Wywołanie samego: __annottations\_\_ daje nam informacje o typach występujących zmiennych.

# %% [markdown]
# Type comments służą również do adnotacji ale Mypy już tego nie wykryje

# %% [markdown]
# Type comments są poprostu komentarzami i można ich użyć w dowolnej wersji Pythona. Używamy ich w następujący sposób # type: typ zmiennej. Poniżej ta sama funkcja circumference,
# z wykorzystaniem komentarzy do opisu zmiennnych.

# %%
import math

def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius


# %%
circumference.__annotations__


# %% [markdown]
# W przypadku funkcji, która zawiera kilka argumentów może to wyglądać w następujący sposób.

# %%
def headline(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)


# %%
def headline(
    text,           # type: str
    width=80,       # type: int
    fill_char="-",  # type: str
):                  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)

#print(headline(1, "tekst", 50))


# %% [markdown]
# Teraz sprawdzimy czy Mypy odczyta typy danych

# %%
# !mypy headline.py

# %% [markdown]
# Typy zmiennych można również przedstawić za pomocą komentarzy, tak jak poniżej

# %%
pi = 3.142  # type: float

# %%
type(pi)

# %% [markdown]
# Adnotacje są oficjalnie zalecanym sposobem typowania danych i będą najlepszym wyborem. Jeśli jednak pracujemy na starszych wersjach Pythona
# powinniśmy skorzystać z komentarzy.

# %% [markdown]
# # **Deck of cards**

# %% [markdown]
# Python zawiera również bardziej skomplikowane typy danych niż str, bool oraz float. Poniżej przedstawimy program który sumuluje grę
# w karty na 4 osoby. Zaczniemy od przedstawienia kodu który tworzy talię 52 kart

# %%
# game.py

import random

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

def create_deck(shuffle=False):
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck):
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}

    for name, cards in hands.items():
        card_str = " ".join(f"{s}{r}" for (s, r) in cards)
        print(f"{name}: {card_str}")

if __name__ == "__main__":
    play()

# %% [markdown]
# Każda karta reprezentowana jest przez jeden kolor i jedną wartość. Talia kart jest listą. Funkcja split dzieli stekst na części oddzielone spacją.
# Funkcja create_deck tworzy nam "nie przetasowaną" talię kart. Deal_hands dzieli karty na czterech graczy. Funkcja play na ten moment jedynie tasuje talię oraz definuje graczy jako P1,P2,P3,P4 i przydziela im karty. Zmienna hands łączy nazwy graczy z odpowaidającymi im listami kart, na zasadzie klucz-wartość: zip(["P1", "P2", "P3", "P4"], (hand1, hand2, hand3, hand4)). Ostatnia pętla for odpowiada za wyświetlenie kart jako ciągu znaków.

# %% [markdown]
# ## Teraz postaramy się opisać zmienne w naszym kodzie

# %%
from typing import Dict, List, Tuple

names: List[str] = ["P1", "P2", "P3"]
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, bool] = {"centered": False, "capitalize": True}


# %% [markdown]
# Należy pamiętać że zmienne w środku listy, słownika czy krotki zawsze piszemy w []. A sama nazwa listy czy słownika zawsze z dużej litery

# %% [markdown]
# Wracając do naszej gry, teraz typ talii kart staje się: List[Tuple[str, str]], więc: 

# %%
def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


# %% [markdown]
# ## Mapowanie i sekwencje

# %% [markdown]
# W pythonie możemy zdefiniować **sekwencje liczb**, np listy lub krotki, które zawierają liczby zmiennoprzecinkowe. Pojawia się tu duck typing ponieważ nie ważne czy jako arugment funkcji podam listę czy krotkę, w wyniku otrzymamy to samo.

# %%
from typing import List, Sequence

"""Funkcja liczy kwadrat każdego elementu z listy lub krotki i zwraca listę."""

def square(elems: Sequence[float]) -> List[float]:
    return [x**2 for x in elems]


# %% [markdown]
# ## Aliasy

# %% [markdown]
# Do opisu deal_hands będziemy wykorzystywali **Aliasy**, dzięki temu nasze adnotacje są bardziej czytelne.

# %%
from typing import List, Tuple

Card = Tuple[str, str] 
Deck = List[Card]

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


# %%
Deck

# %% [markdown]
# W każdej chwili możemy sprawdzić co się kryje pod konkretnym aliasem

# %% [markdown]
# ## Funkcje bez zwracanej wartości

# %% [markdown]
# Jeśli w fukcji nie zadamy wartości zwracanej, to zwraca nam wartość: none.

# %%
"""Funckja wyświetla nazwę gracza"""

def play(player_name):
     print(f"{player_name} plays")


# %%
value = play("gracz")
type(value)


# %% [markdown]
# Jeśli dopiszemy adnotacje do funkcji to mypy stwierdzi, że nie zwraca wartości ponieważ none nie jesteśmy w stanie wykorzystać w żaden sposób.

# %%
def play(player_name: str) -> None:
    print(f"{player_name} plays")

# value = play("gracz")


# %%
# !mypy play.py

# %% [markdown]
# Gdybyśmy nie dodali adnotacji samej wartości zwracanej mypy uzna że wszystko jest okej.

# %%
def play2(player_name: str):
    print(f"{player_name} plays")

# value = play2("gracz")


# %%
# !mypy play2.py

# %%
from typing import NoReturn

def black_hole(text: str) -> NoReturn:
    raise Exception("There is no going back ...")


# %%
black_hole("return")

# %% [markdown]
# Jeśli chcemy żeby funkcja zupełnie niczego nie zwracała to możemy zamiportować typowanie NoRetrun. Wywołując funkcje zawsze dostaniem zastrzeżenie

# %%
