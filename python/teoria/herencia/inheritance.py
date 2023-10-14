class ClasePadre:
	# Método Constructor
	def __init__(self, attr_P1, attr_P2, attr_P3, attr_P4 = "incializado"):
		self.attr_P1 = attr_P1
		self.attr_P2 = attr_P2
		self.attr_P3 = attr_P3
		self.attr_P4 = attr_P4
	
	def acción_1(self):
		print('Soy un método')

class ClaseHija(ClasePadre):
	def __init__(self, attr_P1, attr_P2, attr_P3, attr_H1, attr_H2):#pasasr atributos de las dos clases
		super().__init__(attr_P1, attr_P2, attr_P3) # Llamo al método constructor de la clase padre
    		self.attr_H1 = attr_H1
			self.attr_H2 = attr_H2
#para attr_4 tomma valor de default
		
# Creo un objeto de la clase (instanciar una clase)
instancia_de_mi_clase = ClaseHija("Atributo 1", 2, ["Atributo", "número", 3])

# Consulto atributos (propiedades) del objeto
instancia_de_mi_clase.acción_1()