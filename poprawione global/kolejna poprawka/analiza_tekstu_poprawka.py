import string
from collections import defaultdict
from typing import Dict

with open('tekst.txt', 'r') as plik:
    zawartosc = plik.read()
    slowa = zawartosc.split()
    liczba_slow = len(slowa)
    print(f"Liczba słów w tekście: {liczba_slow}")
    
    statystyki: Dict[str, int] = defaultdict(int)
    for slowo in slowa:
        oczyszczone_slowo = slowo.strip(string.punctuation).lower()
        if oczyszczone_slowo:
            ostatnia_litera = oczyszczone_slowo[-1]
            statystyki[ostatnia_litera] += 1
    
    print("Statystyki końcowych liter:")
    for litera, liczba in statystyki.items():
        print(f"{litera}: {liczba}")