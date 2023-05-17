from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self):
        self._pole = None
        self._obwod = None
    
    @abstractmethod
    def oblicz_pole(self):
        pass
    
    @abstractmethod
    def oblicz_obwod(self):
        pass
    
    def wyswietl_pole(self):
        print(f"Pole: {self.oblicz_pole()}")
    
    def wyswietl_obwod(self):
        print(f"Obwod: {self.oblicz_obwod()}")

class TrojkatRownoboczny(Figura):
    def __init__(self, dlugosc_boku):
        super().__init__()
        self._dlugosc_boku = dlugosc_boku
    
    def oblicz_pole(self):
        return (math.sqrt(3) / 4) * self._dlugosc_boku ** 2
    
    def oblicz_obwod(self):
        return 3 * self._dlugosc_boku