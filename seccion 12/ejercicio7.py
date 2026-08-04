CONTRASENA_CORRECTA = "SENA2026"

intento = ""

while intento != CONTRASENA_CORRECTA:
    intento = input("Introduce la contraseña: ")
    if intento != CONTRASENA_CORRECTA:
        print("Contraseña incorrecta. Inténtalo de nuevo.\n")

print("¡Acceso concedido!")