class Forma:
       def area(self):
           pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Programa de prueba:
def calcular_area(forma):
    return forma.area()

circulo = Circulo(5)
cuadrado = Cuadrado(4)

print(calcular_area(circulo))  # Imprime el área del círculo
print(calcular_area(cuadrado))  # Imprime el área del cuadrado
print(circulo.area())