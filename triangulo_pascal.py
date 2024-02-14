#Triangulo pascal
'''from math import factorial

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
'''

from math import factorial
 
filas_2 = int(input('ingresa numero de filas: '))

for P in range(filas_2):

 for A in range(filas_2 - P + 1):
    print(end=" ")
 for r in range(P + 1):
    numero = factorial(P) // (factorial(P - r) * factorial(r))
    print(numero, end=" ")
 print()
