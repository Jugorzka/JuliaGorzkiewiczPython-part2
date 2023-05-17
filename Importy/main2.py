from main1 import *
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