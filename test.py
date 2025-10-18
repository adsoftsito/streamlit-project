# Tarea 1
# Red de Hopfield
## Jorge Emiliano Pomar A01709338

import numpy as np


# Para Imrpimir
def imprimir_lista(nombre, lista):
    print(nombre, "=", lista)


def imprimir_matriz(nombre, matriz):
    print(nombre, ":")
    for fila in matriz:
        print(fila)


# Paso 1: Definir patrones
# Tamano de los patrones
N = 4

# Paso 2 y 3: Reshape x1 y x2 a 1xN

x1 = np.array([1, 1, 1, 0]).reshape(1, N)[0].tolist()
x2 = np.array([0, 0, 0, 1]).reshape(1, N)[0].tolist()

patrones_guardados = [x1, x2]

# Paso 4: Reemplazar 0 con -1 en X1 y X2
i = 0
while i < len(patrones_guardados):
    patron = patrones_guardados[i]
    j = 0
    while j < len(patron):
        if patron[j] == 0:
            patron[j] = -1
        elif patron[j] == 1:
            patron[j] = 1
        else:
            if patron[j] >= 0:
                patron[j] = 1
            else:
                patron[j] = -1
        j += 1
    i += 1

imprimir_lista("x1 convertido", patrones_guardados[0])
imprimir_lista("x2 convertido", patrones_guardados[1])

# Paso 5: Inicializar tabla de pesos en 0
tabla_pesos = []
i = 0
while i < N:
    fila = []
    j = 0
    while j < N:
        fila.append(0)
        j += 1
    tabla_pesos.append(fila)
    i += 1

# Paso 6 y 7: Obtener transpuesta de X1 y X2, multiplicar por si mismos y sumar (T = X1 + X2)
p = 0
while p < len(patrones_guardados):
    patron = patrones_guardados[p]
    i = 0
    while i < N:
        j = 0
        while j < N:
            # Paso 8: Poner en 0 la diagonal de T
            if i != j:
                tabla_pesos[i][j] += patron[i] * patron[j]
            j += 1
        i += 1
    p += 1

imprimir_matriz("matriz diagonal en 0: ", tabla_pesos)

# Paso 9: Reconocimiento de patron (CASO 1, patron existe)
estado_inicio = [0, 0, 0, 0]

# Paso 4 (de nuevo): Convertir estado_inicio a 1
i = 0
while i < N:
    if estado_inicio[i] == 0:
        estado_inicio[i] = -1
    elif estado_inicio[i] == 1:
        estado_inicio[i] = 1
    else:
        if estado_inicio[i] >= 0:
            estado_inicio[i] = 1
        else:
            estado_inicio[i] = -1
    i += 1

imprimir_lista("estado inicio: ", estado_inicio)

# Paso 10: Comparar y aplicar funcion de activacion
# Parametros de la actualizacion

tope_pasos = 100
pasos = 0

# Copia estado actual
estado_actual = []
i = 0
while i < N:
    estado_actual.append(estado_inicio[i])
    i += 1

while pasos < tope_pasos:
    pasos += 1

    # se calcula nuevo estado a partir del estado actual
    nuevo_estado = []
    i = 0
    while i < N:
        # suma pesos y estado
        campo = 0
        j = 0
        while j < N:
            campo += tabla_pesos[i][j] * estado_actual[j]
            j += 1
        if campo >= 0:
            nuevo_estado.append(1)
        else:
            nuevo_estado.append(-1)
        i += 1

    # evaluar si cambio
    igual = True
    i = 0
    while i < N:
        if nuevo_estado[i] != estado_actual[i]:
            igual = False
            break
        i += 1

    # Paso 11: Si el patron existe, se mantiene
    if igual:
        break

    # si cambio entonces hacemos estado_actual = nuevo_estado
    i = 0
    while i < N:
        estado_actual[i] = nuevo_estado[i]
        i += 1

estado_final = nuevo_estado
imprimir_lista("estado_final", estado_final)
print("pasos =", pasos)

# Paso 12: Si no hay patron, regresar el mas cercano
mejor_patron = None
mejor_dist = 10**9

p = 0
while p < len(patrones_guardados):
    patron = patrones_guardados[p]

    # calcula la distancia entre el estado final y patron
    d = 0
    i = 0
    while i < N:
        if estado_final[i] != patron[i]:
            d += 1
        i += 1

    # si es mejor, guardar como mejor patron
    if d < mejor_dist:
        mejor_dist = d

        mejor_patron = []
        k = 0
        while k < N:
            mejor_patron.append(patron[k])
            k += 1

    p += 1

imprimir_lista("patron mas cercano: ", mejor_patron)
print("distancia: ", mejor_dist)
