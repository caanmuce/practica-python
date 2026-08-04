piso_actual = 1

while True:
    print(f"\n[ Ascensor en el Piso {piso_actual} ]")
    print("1. Subir un piso")
    print("2. Bajar un piso")
    print("3. Ver piso actual")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        if piso_actual < 10:
            piso_actual += 1
            print(f"Subiendo... Ahora estás en el piso {piso_actual}.")
        else:
            print("¡Error! Ya estás en el piso 10. No se puede subir más.")
            
    elif opcion == "2":
        if piso_actual > 1:
            piso_actual -= 1
            print(f"Bajando... Ahora estás en el piso {piso_actual}.")
        else:
            print("¡Error! Ya estás en el piso 1. No se puede bajar más.")
            
    elif opcion == "3":
        print(f"Te encuentras actualmente en el piso {piso_actual}.")
        
    elif opcion == "4":
        print("Saliendo del simulador de ascensor.")
        break
    else:
        print("Opción no válida.")