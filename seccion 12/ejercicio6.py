suma_notas = 0
cantidad_notas = 5

for i in range(1, cantidad_notas + 1):
    nota = float(input(f"Ingrese la nota {i}: "))
    suma_notas += nota

promedio = suma_notas / cantidad_notas
print(f"\nEl promedio final es: {promedio:.2f}")