wiek = input ('Podaj swój wiek: ')
A2 = True if input("Czy masz prawo jazdy kategorii A2?") \
    in ('t', "ta", "Tak", "T") else False
odiluA2= 0
if A2:
    odiluA2 = int(input("Jak długo masz A2? Podaj ilość lat: "))
if wiek >= 24 or (A2 and wiek >= 20 and odiluA2>=2):
    print ("Możesz przystąpić do egzaminu na prawo jazdy na kategorię A")
else:
    print ("Nie możesz przystąpić do egzaminu na prawo jazdy na kategorię A")