# Clave correcta predefinida
CLAVE_CORRECTA = "1234"
intentos_maximos = 3

for intento in range(1, intentos_maximos + 1):
    clave_ingresada = input(f"Intento {intento}/{intentos_maximos} - Ingrese su clave de 4 dígitos: ")
    
    if clave_ingresada == CLAVE_CORRECTA:
        print("¡Bienvenido! Ingreso exitoso.")
        break
else:
    print("Cuenta bloqueada. Ha superado el número máximo de intentos.")