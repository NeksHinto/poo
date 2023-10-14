class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice Woof!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau!"

perro = Perro("Buddy")
gato = Gato("Whiskers")

print(perro.hablar())  # Salida: "Buddy dice Woof!"
print(gato.hablar())   # Salida: "Whiskers dice Miau!"