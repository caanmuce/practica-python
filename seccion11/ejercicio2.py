total_clientes = 10
suma_calificaciones = 0
calificaron_con_5 = 0
calificaron_1_o_2 = 0
clientes_satisfechos = 0

for i in range(1, total_clientes + 1):
    while True:
        try:
            nota = int(input(f"Cliente {i} - Ingrese su calificación (1 al 5): "))
            if 1 <= nota <= 5:
                break
            print("Por favor, ingrese un número válido entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            
    suma_calificaciones += nota
    
    if nota == 5:
        calificaron_con_5 += 1
    elif nota == 1 or nota == 2:
        calificaron_1_o_2 += 1
        
    if nota >= 4:
        clientes_satisfechos += 1

promedio = suma_calificaciones / total_clientes
porcentaje_satisfaccion = (clientes_satisfechos / total_clientes) * 100

print("\n--- RESULTADOS DE LA ENCUESTA ---")
print(f"Promedio general: {promedio:.2f}")
print(f"Clientes que calificaron con 5: {calificaron_con_5}")
print(f"Clientes que calificaron con 1 o 2: {calificaron_1_o_2}")
print(f"Porcentaje de satisfacción (Notas 4 y 5): {porcentaje_satisfaccion}%")