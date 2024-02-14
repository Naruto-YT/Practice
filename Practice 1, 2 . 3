Practica
#1 
# #Crea una función que tome un y devuelva la primera letra en mayúsculas y el resto en minúsculas.
#Hacer que la primera letra este en mayuscula y las demas en miniscula
def primer_mayusc(string):
    lista = []
    for x in range(len(string)):
        if x == 0:
            lista.append(string[x].upper())
        else: 
            lista.append(string[x].lower())
    return ''.join(lista)

print(primer_mayusc("hola mundo"))
print(primer_mayusc("todo esta perdido"))

def primer_mayusc2(string):
    string = string.lower()
    lista_del_string = list(string)
    lista_del_string[0] = lista_del_string[0].upper()
    return''.join(lista_del_string)

print(primer_mayusc2("todo esta perdido de nuevo"))


#Practica 2
#Dada una lista entero, identifica si la secuencia [10, 20, 30]esta en algun lugar de la lista

def chequeo_sec(lista):
    i = 0
    while i < (len(lista) - 2):
        if lista[i] == 10 and lista[i+1] == 20 and lista[i+2] == 30:
            return True
        else:
                i + 1
        return False

print(chequeo_sec([10,20,30]))
print(chequeo_sec([10,10,30]))
print(chequeo_sec([10,20,20,49,10,20,30]))

#Crea un programa capaz de encontrar el maximo comun divisor entre dos numeros dados
#Forma 1
def mcd(a, b):
    if b == 0:
        return a
    else: 
            return mcd(b, a%b)

print(mcd(129,116))

#forma 2
def mcd_2(x, y):
    if x > y:
        menor = y
    else:
        menor = x
    for i in range(1, menor + 1):
        if x % i == 0 and y % i == 0:
            mcd = i
    return mcd

print(mcd_2(129, 116))

#forma #3

def mcd_3(x, y):
    while y:
        x, y = y, x % y
    return x

print(mcd_3(129, 116))

#crea un programa que reciba una frase y duevuelva un diccionario con la cantidad de veces wue se repita cada palabra con una frese
def dic_contador():
    parrafo = input('escribe tu frase')

    contador = {}
    palabras = parrafo.replace(',', '').replace(',', '').lower().split()
    
    for elem in palabras:
        if elem in contador:
            contador[elem] += 1
        else:
            contador[elem] = 1
    
    return(contador)

print(dic_contador())

#Triangulo pascal
from math import factorial

filas = int(input('Ingresa el número de filas: '))


# Loop principal 
for n in range(filas):
    # Espacios en blanco para alinear el triángulo
    for j in range(filas - n + 1):
        print(end=" ")

    # Loop para imprimir los números
    for r in range(n + 1):
        numero = factorial(n) // (factorial(n - r) * factorial(r))
        print(numero, end=" ")

    # Salto de línea después de cada fila
    print()
