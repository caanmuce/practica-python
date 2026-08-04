meta = float(input("¿Cuál es tu meta de ahorro total?: $"))
ahorro_mensual = float(input("¿Cuánto dinero vas a ahorrar mensualmente?: $"))

if ahorro_mensual <= 0:
    print("El ahorro mensual debe ser mayor a 0 para poder alcanzar la meta.")
else:
    meses = 0
    ahorro_acumulado = 0
    
    while ahorro_acumulado < meta:
        ahorro_acumulado += ahorro_mensual
        meses += 1
        
    print(f"\n¡Meta alcanzada! Necesitas {meses} meses para ahorrar ${meta:,.2f}.")
    print(f"Total final ahorrado: ${ahorro_acumulado:,.2f}")