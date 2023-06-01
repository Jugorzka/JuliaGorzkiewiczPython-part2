import random

x = random.randint(0, 100)
ilosc_prob = 0  

while True:
    a = int(input('Podaj liczbę: '))
    ilosc_prob += 1  

    if a == x:
        print('Brawo, to jest ta liczba :D')
        print('Odgadłeś liczbę po', ilosc_prob, 'próbach.')  
        c = input("Napisz 'tak', jeśli chcesz zagrać ponownie: ")
        if c == "tak":
            x = random.randint(0, 100)  
            ilosc_prob = 0  
            continue
        else:
            break
    elif a < x:
        print("Twoja liczba jest mniejsza od szukanej")
    elif a > x:
        print("Twoja liczba jest większa od szukanej")
