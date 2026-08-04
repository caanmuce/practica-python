numero = int(input("Ingrese el número para ver su tabla de multiplicar: "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")