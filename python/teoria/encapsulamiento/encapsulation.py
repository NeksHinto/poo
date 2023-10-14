class MiClase:
	def __init__(self, __attr_privado = "valor"):
		self.__attr_privado = __attr_privado

	def metodo_privado(self):
		return f"Holis"

	def get_attr_privado(self):
		return self.__attr_privado
	
	def set_attr_privado(self, valor_del_usuario):
		# validaciones
		self.__attr_privado = valor_del_usuario
	
objeto = MiClase()
# print(objeto.__attr_privado) #si no fuera privado imrpimiría "valor"
# Para evitar que el user 
# - modifique directamente haciendo objeto.__attr_privado = "hola", o
# - acceda directamente haciendo objeto.__attr_privado
# usamos getters y setters
print(objeto.metodo_privado())