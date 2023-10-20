def encrypt(message: str, password: str) -> str:
    lista_message:list=[]
    lista_password:list=[]
    lista_encriptados:list=[]
    respuesta:str=""

    for letra in message:
        lista_message.append(ord(letra))
    largo_message = len(lista_message)


    for letra in password:
        lista_password.append(ord(letra))
    #print(lista_password)
    largo_password = len(lista_password)

    for i in range(largo_message): # largo_mensaje = 23, largo_password = 6
        # "badke56 wonderful World!", "badke5" con el 6 daría error
        if i < largo_password: #la validación es con el password (ver si vuelvo a inicio o no CUANDO i >= largo_password)
            #print(i) 
            lista_encriptados.append(lista_password[i] ^ lista_message[i])
            # print(lista_encriptados)
        else:
            p = i % largo_password # 12 - 5 - 1 =  6 para que no salte la b, con el módulo me aseguro que, al ser un resto, nunca sea más grande que el divisor
            #la resta sirve para un largo fijo, no uno variable
            #menor al último índice (un valor menor a largo)
            lista_encriptados.append(lista_password[p] ^ lista_message[i])


    for numero in lista_encriptados:
        respuesta+=chr(numero)

    return respuesta

print(encrypt("ja", "badkey"))


def encrypt_with_char(message: str, key: str) -> str:
    lista:list=[]
    lista_encriptados:list=[]
    key=ord(key)
    respuesta:str=""

    for letra in message:
        lista.append(ord(letra))

    for numero in lista:
        lista_encriptados.append(numero^key) #con ^ se encripta usando el xor

    for numero in lista_encriptados:
        respuesta+=chr(numero)

    return respuesta