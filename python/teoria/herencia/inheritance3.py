class A:
	pass

class F:
	def hablar(self):
		print("Hola desde F")

class B(A):
	pass

class C(F):
	pass

class D(B, C):
	pass

d = D()
d.hablar()
# sin super empieza por la clase a la que pertenece la instancia
# con super empieza por la clase padre más cercana o la primera en la lista ( como en el caso de D(B,C))