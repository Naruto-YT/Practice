#Crea un programa capaz de encontrar el maximo comun divisor entre dos numeros dados
#Forma 1
'''
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

'''

#replica de la forma #1
def minimo_comun_divisor(a, b):
    if b == 0:
        return a
    else:
        return minimo_comun_divisor(b, a%b)
print(minimo_comun_divisor(129, 117))

#forma 2 - replica
def mcv3(p, a):
    if p > a:
        menor = a
    else:
        menor = p
    for i in range(1, menor + 1):
        if p % i == 0 and  a % i == 0:
            mcv3 = i
    return mcv3
print(mcv3(129, 116))

#forma 3
''' def mcd_3(x, y):
    while y:
        x, y = y, x % y
    return x

print(mcd_3(129, 116)) '''
def mvc4(A, Y):
    while Y:
        A, Y = Y, A % Y
    return A

print(mvc4(129,116))
