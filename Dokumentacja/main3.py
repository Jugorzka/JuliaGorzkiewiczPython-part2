def add(a: float, b: float) -> float:
    """Dodaje dwie liczby"""
    return a + b


def subtract(x: float, y: float) -> float:
    """Odejmuje drugą liczbę od pierwszej"""
    return x - y


def multiply(x: float, y: float) -> float:
    """Mnoży dwie liczby"""
    return x * y


def divide(x: float, y: float) -> float:
    """Dzieli pierwszą liczbę przez drugą"""
    return x / y


while True:
    operation = input("Wybierz operację (+, -, *, /) lub wpisz 'a', aby zakończyć: ")
    if operation == "a":
        break
    if operation not in ["+", "-", "*", "/"]:
        print("Niepoprawna operacja.")
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
    print(f"Wynik: {result}")