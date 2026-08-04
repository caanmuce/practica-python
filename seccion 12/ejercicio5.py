suma_total = 0

for i in range(1, 11):
    num = float(input(f"Ingrese el número {i}: "))
    suma_total += num  # Acumulador

print(f"\nLa suma total de los 10 números es: {suma_total}")