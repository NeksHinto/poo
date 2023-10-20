from functools import reduce

def sum_of_multiples(limit, multiples):
    valores_definitivos=[]
    for i in range(1,limit):
        for j in multiples:
            if j!=0:
                if i%j==0 and i not in valores_definitivos: #evitar repeticiones por ser múltiplo de 5 Y de 3. Acá pide or
                    valores_definitivos.append(i)
    resultado=0
    for k in valores_definitivos:
        resultado+=k
    return resultado


#-----------------------------------------------------------------------------------------------
def sum_of_multiples(limit, multiples):
    if len(multiples)==0: #por si la longitud es 0
        return 0
    elif len(multiples)!=0 and 0 in multiples: #para que no falle al dividir por cero
        multiples.remove(0)

    lambda_function = lambda x: any(x%j==0 for j in multiples)
    multiples_list=list(filter(lambda_function, range(1,limit))) # por cada numero del range, aplica la función lambda y si es divisor de por lo menos 1 de multiples, lo agrega a la lista
    return reduce(lambda x,y: x+y, multiples_list,0) #el x acumula y pasa a ser la suma, el y itera, le paso la función


#-----------------------------------------------------------------------------------------------

def my_filter(limit, multiples):
    valores_definitivos = []
    for i in range(1, limit):
        for j in multiples:
            if j != 0:
                if i % j == 0 and i not in valores_definitivos:  # evitar repeticiones por ser múltiplo de 5 Y de 3. Acá pide or
                    valores_definitivos.append(i)
    return valores_definitivos
#pasar alguna de las condiciones de my_filter a un my_map (reduce funciona con un map por atrás)
#my_reduce/filter puede ser de orden mayor porque recibe my_map


def my_reduce(valores):
    resultado=0
    for numero in valores:
        resultado+=numero
    return resultado

def sum_of_multiples(limit, multiples, función_1, función_2): #NO TENGO QUE PASAR LAS FUNCIONES EN LOS PARÁMETROS?
    valores=función_1(limit, multiples)
    respuesta=función_2(valores)
    return respuesta

sum_of_multiples(20,[3,5],my_filter, my_reduce)