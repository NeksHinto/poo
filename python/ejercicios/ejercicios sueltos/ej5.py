def numeros_pares(n, m):
    respuestas = []
    for numero in range(n, m + 1):
        numero = str(numero)
        is_even:bool = True
        for digito in numero:
            if int(digito) % 2 != 0:
                is_even=False
                break
        
        if is_even==True:
            respuestas.append(int(numero))

    return respuestas

print(numeros_pares(2,40))