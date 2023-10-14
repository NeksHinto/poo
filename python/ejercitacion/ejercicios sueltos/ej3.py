def matriz_sin_repetir_loop(n:int, m:int)-> list[list]:
    lista_vacia:list=[]
    
    for i in range(n): 
        fila = []  # Se crea una fila vacía en cada iteración de i
        for j in range(m): 
            fila.append(i * j)  # Se agregan elementos a la variable fila
        lista_vacia.append(fila)  # Se agrega la fila completa a la lista

    return lista_vacia

resultado1 = matriz_sin_repetir_loop(3, 5)
print(resultado1)

def matriz(n:int, m:int)-> list[list]:
    lista_vacia:list=[]

    for i in range(n):
        lista_vacia.append([])
    for lista in lista_vacia:
        for j in range(m):
            lista.append(j*i)
    
    return lista_vacia

resultado2 = matriz(3, 5)
print(resultado2)

# lista_vacia.append([]) # cuando i = 0 -> lista_vacia = [[]], cuando i = 1 -> lista_vacia = [[0, 0, 0..], []]