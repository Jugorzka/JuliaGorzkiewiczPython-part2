lista = {"burak", "cukinia", "pomidor", "cytryna","ananas", "papryka", "dynia"}
litera = input("Podaj literę: ")
for element in lista:
    if element.startswith(litera):
        print(element, end= " ")