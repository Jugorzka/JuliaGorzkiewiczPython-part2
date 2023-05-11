def dodaj(a: float, b: float) -> float:
    """
    Dodaje dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik dodawania
    """
    return a + b

def odejmij(a: float, b: float) -> float:
    """
    Odejmuje dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik odejmowania
    """
    return a - b

def pomnoz(a: float, b: float) -> float:
    """
    Mnoży dwie liczby.

    :param a: pierwsza liczba
    :param b: druga liczba
    :return: wynik mnożenia
    """
    return a * b

def podziel(a: float, b: float) -> Union[float, None]:
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
    wybor: str = input("Wybierz opcję: ")

   
    if wybor == "0":
        print("Dziękuję za skorzystanie z kalkulatora!")
        break

  
    a: float = float(input("Podaj pierwszą liczbę: "))
    b: float = float(input("Podaj drugą liczbę: "))

   
    if wybor == "1":
        wynik: float = dodaj(a, b)
        print("Wynik dodawania:", wynik)
    elif wybor == "2":
        wynik: float = odejmij(a, b)
        print("Wynik odejmowania:", wynik)
    elif wybor == "3":
        wynik: float = pomnoz(a, b)
        print("Wynik mnożenia:", wynik)
    elif wybor == "4":
        wynik: Union[float, None] = podziel(a, b)
        if wynik is not None:
            print("Wynik dzielenia:", wynik)
    else:
        print("Nieprawidłowa opcja!")
