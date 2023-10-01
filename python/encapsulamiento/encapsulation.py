class MiClase:
	def __init__(self, __attr_privado = "valor"):
		self.__attr_privado = __attr_privado

	def metodo_privado(self):
		return f"Holis"
	
objeto = MiClase()
# print(objeto.__attr_privado) #si no fuera privado imrpimiría "valor"
print(objeto.metodo_privado())