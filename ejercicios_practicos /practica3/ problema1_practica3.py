'''
Nombre: Cristopher López Jiménez
Asignatura: Programación de Redes
'''

datos = []

for i in range(5):
    dato = int(input("Ingresa un dato entero: "))
    datos.append(dato)

tuplaDatos = tuple(datos)

def desplegar_tupla(tupla):
    print("Contenido de la tupla:")
    for dato in tupla:
        print(dato)

desplegar_tupla(tuplaDatos)

print("Longitud de la tupla:", len(tuplaDatos))

def suma_tupla(tupla):
    total = sum(tupla)
    print("La suma de los elementos de la tupla es:", total)
    return total

suma_tupla(tuplaDatos)

tuplaDatos = tuplaDatos[:-1] + (tuplaDatos[-1] * 2,)

print("Contenido de la tupla después de reemplazar el último elemento:", tuplaDatos)

def multiplica_tupla(tupla):
    resultado = 1
    for dato in tupla:
        resultado *= dato
    print("El resultado de la multiplicación de los elementos de la tupla es:", resultado)
    return resultado

multiplica_tupla(tuplaDatos)
tupla1 = (1, 2, 3, 4)
resultado_suma = tuple(x + y for x, y in zip(tuplaDatos, tupla1))
print("Resultado de sumar las dos tuplas:", resultado_suma)
