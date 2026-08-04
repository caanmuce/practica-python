stock = 50

while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print(f"Stock actual: {stock} unidades")
    print("1. Vender producto")
    print("2. Agregar inventario")
    print("3. Consultar stock")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        cantidad = int(input("Cantidad a vender: "))
        if cantidad <= stock:
            stock -= cantidad
            print(f"Venta realizada. Se vendieron {cantidad} unidades.")
        else:
            print("Error: No hay suficiente stock para realizar la venta.")
            
    elif opcion == "2":
        cantidad = int(input("Cantidad a agregar al inventario: "))
        if cantidad > 0:
            stock += cantidad
            print(f"Inventario actualizado. Se agregaron {cantidad} unidades.")
        else:
            print("La cantidad debe ser mayor a cero.")
            
    elif opcion == "3":
        print(f"El stock actual disponible es de {stock} unidades.")
        
    elif opcion == "4":
        print("Saliendo del sistema de inventario. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")