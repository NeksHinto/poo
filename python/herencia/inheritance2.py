class ClasePadre1:
	# Método Constructor
	def __init__(self, attr_P1_1, attr_P1_2, attr_P1_3):
		self.attr_P1_1 = attr_P1_1
		self.attr_P1_2 = attr_P1_2
		self.attr_P1_3 = attr_P1_3
	
	def acción_P1(self):
		print('Soy un método')

class ClasePadre2:
	def __init__(self, attr_P2_1):
		self.attr_P2_1 = attr_P2_1
	
	def acción_P2(self):
		print(f'{self.attr_P2_1}')

# Multiherencia
class ClaseHija(ClasePadre1, ClasePadre2):
	def __init__(self, attr_P1_1, attr_P1_2, attr_P1_3, attr_P2_1, attr_H1, attr_H2):
		ClasePadre1.__init__(attr_P1_1, attr_P1_2, attr_P1_3)
		#no se usa super() sino clase en particular a la que se hacer eferencia
		ClasePadre2.__init__(attr_P2_1)
		self.attr_H1 = attr_H1
		self.attr_H2 = attr_H2
		
	def acción_P2(self):
		print("Sobreescribo método de ClasePadre2")

	def acción_H1(self):
		# print(f'{self.acción_P2}')
		print(f'{super().acción_P2}')
		
# Creo un objeto de la clase (instanciar una clase)
instancia_de_mi_clase = ClaseHija("Atributo 1", 2, ["Atributo", "número", 3])

# Consulto atributos (propiedades) del objeto
instancia_de_mi_clase.acción_H1()