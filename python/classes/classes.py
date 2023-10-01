class Auto:

    def __init__(self, marca, color, cant_km, encendido = False):
        self.marca = marca
        self.color = color
        self.cant_km = cant_km
        self.encendido = encendido
    
    def __str__(self):
        return f"Clase Auto = Marca: {self.marca}, color: {self.color} y cantidad km: {self.cant_km}"
    
    def arrancar(self): 
        self.encendido = True
        return "¡Arrancó el auto!"

auto_lari = Auto("Ford", "rojo", 450)
auto_nicky = Auto("Honda", "azul", 500)

print(auto_lari.arrancar())
print(auto_lari.encendido) #para ver si se ejecutó bien


