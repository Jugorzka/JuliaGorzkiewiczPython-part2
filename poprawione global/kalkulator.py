def add(a, b):
    """Dodawanie"""
    return a + b


def subtract(x, y):
    """Odejmowanie"""
    return x - y


def multiply(x, y):
    """Mnozenie"""
    return x * y


def divide(x, y):
    """Dzielenie"""
    if y == 0:
        print("Błąd: Nie można dzielić przez zero.")
        return None
    return x / y


while True:
    operation = input("Wybierz operację (+, -, *, /) lub wpisz 'a', aby zakończyć: ")
    if operation == "a":
        print('Dziękuję za skorzystanie z kalkulatora!')
        break
    if operation not in ["+", "-", "*", "/"]:
        print("Wybrano niepoprawną operacje.")
        continue
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
        if result is None:
            continue
    print(f"Wynik: {result}")
