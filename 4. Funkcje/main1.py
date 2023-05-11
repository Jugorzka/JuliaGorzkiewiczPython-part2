def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        print("Nie można dzielić przez zero!")
        return None
    else:
        return a / b

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("0. Wyjście")
    wybór = input("Wybierz opcję: ")

    if wybór == "0":
        print("Dziękuję za skorzystanie z kalkulatora!")
        break

    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    if wybór == "1":
        wynik = dodaj(a, b)
        print("Wynik dodawania:", wynik)
    elif wybór == "2":
        wynik = odejmij(a, b)
        print("Wynik odejmowania:", wynik)
    elif wybór == "3":
        wynik = pomnoz(a, b)
        print("Wynik mnożenia:", wynik)
    elif wybór == "4":
        wynik = podziel(a, b)
        if wynik is not None:
            print("Wynik dzielenia:", wynik)
    else:
        print("Nieprawidłowa opcja!")
