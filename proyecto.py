import timeit

def fibonacci_iter(n):
    """
    Genera una serie de Fibonacci iterativa hasta el n-ésimo número.
    """
    fib_series = [0, 1]
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
    return fib_series

def fibonacci_rec(n):
    """
    Calcula el n-ésimo número de Fibonacci recursivamente.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def medir_tiempo(func):
    """
    Mide el tiempo de ejecución de una función y devuelve el resultado de la función.
    """
    resultado = func()
    tiempo_medido = timeit.timeit(func, number=1)
    return resultado, tiempo_medido

# Llama a las funciones y mide el tiempo de ejecución
resultado_iterativo, tiempo_iterativo = medir_tiempo(lambda: fibonacci_iter(10))
print(f"Numero: {resultado_iterativo}")
print(f"Tiempo de ejecución de FIBONACCI ITERATIVO: {tiempo_iterativo} segundos")

resultado_recursivo, tiempo_recursivo = medir_tiempo(lambda: fibonacci_rec(10))
print(f"Numero: {resultado_recursivo}")
print(f"Tiempo de ejecución FIBONACCI RECURSIVO: {tiempo_recursivo} segundos")
