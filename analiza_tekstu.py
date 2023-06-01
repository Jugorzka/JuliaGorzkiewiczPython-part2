from collections import defaultdict
from typing import Dict

with open('tekst.txt', 'r') as tekst:
    a = tekst.read()
    words = a.split()
    num_words = len(words)
    print(f"Liczba słów w tekście wynosi: {num_words}")
    
    stats: Dict[str, int] = defaultdict(int)
    for word in words:
        last_letter = word[-1].lower()
        stats[last_letter] += 1
    
    print("Statystyka końcowych liter:")
    for letter, count in stats.items():
        print(f"{letter}: {count}")