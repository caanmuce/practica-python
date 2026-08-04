notas = []
for i in range(1, 5):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

promedio = sum(notas) / 4
print(f"Promedio inicial: {promedio:.2f}")

if promedio >= 3.0:
    print("¡Felicidades! Has aprobado la materia.")
else:
    print("El promedio es menor a 3.0. Debes presentar una nota de recuperación.")
    nota_recuperacion = float(input("Ingrese la nota obtenida en la recuperación: "))
    
    # Reemplazamos la nota más baja con la de recuperación
    notas.remove(min(notas))
    notas.append(nota_recuperacion)
    
    nuevo_promedio = sum(notas) / 4
    print(f"Nuevo promedio tras recuperación: {nuevo_promedio:.2f}")
    
    if nuevo_promedio >= 3.0:
        print("Aprobado tras la recuperación.")
    else:
        print("Reprobado. No se alcanzó el puntaje mínimo de 3.0.")
        3