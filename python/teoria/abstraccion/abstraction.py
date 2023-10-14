from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def conducir(self):
        pass

class Automovil(Vehiculo): 
    def __init__(self, marca, radio): #si lo hereda inicializar lo de padre
        super().__init__(marca)
        self.radio = radio

    def conducir(self): #no necesita inicializar por herencia 
        return f"Conduciendo un automóvil de {self.marca}"

class Motocicleta(Vehiculo):#no hay constructor de motocicleta (con super, etc) porque no agrega nada que no este en vehculo
    def conducir(self):
        return f"Conduciendo una motocicleta de {self.marca}"

automovil = Automovil("Toyota", "ASPEN")
motocicleta = Motocicleta("Honda")

print(automovil.conducir())    # "Conduciendo un automóvil de Toyota"
print(motocicleta.conducir())  # "Conduciendo una motocicleta de Honda"