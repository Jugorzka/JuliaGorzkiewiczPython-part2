class Czytelnik:
    def __init__(self, imie: str, nazwisko: str, pesel: str, numer_telefonu: str, adres_email: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.numer_telefonu = numer_telefonu
        self.adres_email = adres_email
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko}, PESEL: {self.pesel}"
czytelnik1 = Czytelnik("Julia", "Kowalska", "12355559901", "123-555-789", "julia.kowalska@gmail.com")
czytelnik2 = Czytelnik("Klaudia", "Nowak", "89034545678", "987-333-321", "klaudia.nowak@wp.com")
