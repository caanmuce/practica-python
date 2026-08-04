total_vendedores = 5
vendedor_top = ""
max_ventas = -1
suma_ventas = 0
superaron_millon = 0

for i in range(1, total_vendedores + 1):
    nombre = input(f"Nombre del vendedor {i}: ")
    ventas = float(input(f"Monto total de ventas de {nombre}: $"))
    
    suma_ventas += ventas
    
    if ventas > max_ventas:
        max_ventas = ventas
        vendedor_top = nombre
        
    if ventas > 1000000:
        superaron_millon += 1

promedio_ventas = suma_ventas / total_vendedores

print("\n--- RESULTADOS DEL CONCURSO ---")
print(f"Vendedor con más ventas: {vendedor_top} (${max_ventas:,.2f})")
print(f"Promedio general de ventas: ${promedio_ventas:,.2f}")
print(f"Vendedores que superaron el $1.000.000: {superaron_millon}")