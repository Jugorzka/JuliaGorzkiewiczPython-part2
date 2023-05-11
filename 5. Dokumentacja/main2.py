def dodaj(a, b):
    """
    Dodaje dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik dodawania
    """
    return a + b

def odejmij(a, b):
    """
    Odejmuje dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik odejmowania
    """
    return a - b

def pomnoz(a, b):
    """
    Mnoży dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik mnożenia
    """
    return a * b

def podziel(a, b):
    """
    Dzieli dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik dzielenia lub None, jeśli druga liczba wynosi 0
    """
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
    wybor = input("Wybierz opcję: ")

   
    if wybor == "0":
        print("Dziękuję za skorzystanie z kalkulatora!")
        break

  
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

   
    if wybor == "1":
        wynik = dodaj(a, b)
        print("Wynik dodawania:", wynik)
    elif wybor == "2":
        wynik = odejmij(a, b)
        print("Wynik odejmowania:", wynik)
    elif wybor == "3":
        wynik = pomnoz(a, b)
        print("Wynik mnożenia:", wynik)
    elif wybor == "4":
        wynik = podziel(a, b)
        if wynik is not None:
            print("Wynik dzielenia:", wynik)
    else:
        print("Nieprawidłowa opcja!")
