import random
from typing import Set

# wczytanie list imion i nazwisk
with open('imiona.txt') as f:
    imiona = [line.strip() for line in f]

with open('nazwiska.txt') as f:
    nazwiska = [line.strip() for line in f]

# pobranie liczby kombinacji od użytkownika
liczba_kombinacji = int(input('Podaj liczbę kombinacji: '))

# wygenerowanie losowych kombinacji imion i nazwisk
kombinacje: Set[str] = set()
while len(kombinacje) < liczba_kombinacji:
    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    kombinacja = f'{imie} {nazwisko}'
    kombinacje.add(kombinacja)

# zapisanie kombinacji do pliku
with open('kombinacje.txt', 'w') as f:
    f.write('\n'.join(kombinacje))
