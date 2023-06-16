wiek = int(input('Podaj swój wiek: '))  

A2 = input('Czy masz prawo jazdy od conajmniej 2 lat? (tak/nie)')

if wiek >= 24 or (A2 == 'tak' and wiek >= 20):
    print("Możesz przystąpić do egzaminu na prawo jazdy na kategorię A")
else:
    print("Nie możesz przystąpić do egzaminu na prawo jazdy na kategorię A")
