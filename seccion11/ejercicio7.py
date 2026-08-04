positivos = 0
negativos = 0
pares = 0
impares = 0
maximo = None

print("Por favor, ingrese 15 números:")
for i in range(1, 16):
    num = float(input(f"Número {i}: "))
    
    # Inicializar el máximo con el primer número ingresado
    if maximo is None or num > maximo:
        maximo = num
        
    # Evaluar si es positivo o negativo (el 0 se toma como neutral en este conteo)
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
        
    # Evaluar si es par o impar (aplicado a enteros para evitar inconsistencias)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- ANÁLISIS DE LOS NÚMEROS ---")
print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos: {negativos}")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
print(f"El número más grande fue: {maximo}")