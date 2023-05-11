slowo = input("Podaj słowo: ")

if slowo == slowo[::-1]:
    print("Słowo", slowo, "jest palindromem!")
else:
    print("Słowo", slowo, "nie jest palindromem.")
