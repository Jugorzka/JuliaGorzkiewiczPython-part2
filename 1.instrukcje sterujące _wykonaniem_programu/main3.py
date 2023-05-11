import random
x = random.randint(0,100)

while(True):
    a = int(input('Podaj liczbę: '))
    if a == x:
        print ('Brawo to jest ta liczba :D')
        c = input("Napisz tak jeśli chcesz zagrać ponownie: ")
        if c == "tak":
                x = int(input('Podaj liczbę: '))
                continue
        else: 
            break
    elif a < x:
        print ("Twoja liczba jest mniejsza od szukanej")
    elif a > x:
        print ("Twoja liczba jest większa od szukanej")
