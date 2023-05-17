class Czytelnik:
    def __init__(self, imie: str, nazwisko: str, pesel: str, numer_telefonu: str, adres_email: str):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__pesel = pesel
        self.__numer_telefonu = numer_telefonu
        self.__adres_email = adres_email
    
    def __str__(self):
        return f"{self.__imie} {self.__nazwisko}, PESEL: {self.__pesel}"
    
    def get_imie(self):
        return self.__imie
    
    def get_nazwisko(self):
        return self.__nazwisko
    
    def get_pesel(self):
        return self.__pesel
    
    def get_numer_telefonu(self):
        return self.__numer_telefonu
    
    def get_adres_email(self):
        return self.__adres_email
