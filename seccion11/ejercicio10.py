temperaturas = []
dias_calurosos = 0

print("Registro de temperaturas de la semana:")
for i in range(1, 8):
    temp = float(input(f"Día {i} - Temperatura (°C): "))
    temperaturas.append(temp)
    
    if temp > 30:
        dias_calurosos += 1

maxima = max(temperaturas)
minima = min(temperaturas)
promedio_semanal = sum(temperaturas) / len(temperaturas)

print("\n--- REPORTE CLIMÁTICO SEMANAL ---")
print(f"Temperatura más alta: {maxima}°C")
print(f"Temperatura más baja: {minima}°C")
print(f"Promedio semanal: {promedio_semanal:.2f}°C")
print(f"Días que superaron los 30°C: {dias_calurosos}")