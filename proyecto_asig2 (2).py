def verificar_coindice(vec):
    conteo1 = 0
    for val in enumerate(vec):
        conteo1 += 1
        if val[0] == val[1]:
            print(f"El índice {val[0]} coincide con el valor {val[1]} en el vector.")
        elif val[0] > val[1]:
            print(f"No hay ninguna coincidencia entre el índice {val[0]} y el valor {val[1]} en el vector.")
        else:
            print(f"No hay ninguna coincidencia entre el índice {val[0]} y el valor {val[1]} en el vector.")
    print(f"Conteo 1: ", conteo1)


# implementacion:
prueba = [5, 4, 3, 2, 1, 0]  # Cambiar cualquier número del arreglo para hacer la verificación
resultado = verificar_coindice(prueba)

print(f" " + resultado)

# ------------------------------------------------------------------------------------------------------------------------


def contar_combinaciones(X, N, num_actual=1, suma_actual=0):
    # Caso base: si la suma actual es igual a X, se ha encontrado una combinación válida
    if suma_actual == X:
        return 1

    # Inicializar el contador de combinaciones
    conteo2 = 0

    # Iterar desde num_actual hasta la raíz N-ésima de X
    for num in range(num_actual, int(X ** (1/N)) + 1):
        conteo2 += 1
        nueva_suma = suma_actual + num ** N
        # Llamada recursiva con el próximo número y la nueva suma
        conteo2 += contar_combinaciones(X, N, num + 1, nueva_suma)
    return conteo2


# implementacion

resultado = contar_combinaciones(13, 2)
print(f" " + resultado)




# -------------------------------------------------------------=---------------------------------------------


def super_digit(n):
    # Caso base: si n tiene un solo dígito, su superdígito es n
    if len(str(n)) <= 1:
        return n
    # Calcular la suma de los dígitos de n
    suma_digs = sum(int(digito) for digito in str(n))

    # Llamar recursivamente a la función con la suma de los dígitos como nuevo n
    return suma_digs

# implementacion
resultado = super_digit(85)
print(f" " + resultado)   