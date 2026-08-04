edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Acceso denegado. Eres menor de edad.")
else:
    genero = input("Ingrese su género (M para masculino, F para femenino): ").strip().upper()
    
    if genero == "F":
        print("¡Acceso concedido! Las mujeres ingresan gratis.")
    elif genero == "M":
        print("Acceso concedido. Los hombres pagan $20.000.")
    else:
        print("Género no reconocido, pero cumples con la edad mínima de ingreso.")