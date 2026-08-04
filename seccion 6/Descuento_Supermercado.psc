Algoritmo Descuento_Supermercado
	
    Definir totalCompra, descuento, totalPagar Como Real
    Definir numero Como Entero
	
    Escribir "Ingrese el total de la compra:"
    Leer totalCompra
	
    Escribir "Ingrese el numero escogido al azar:"
    Leer numero
	
    Si numero < 74 Entonces
        descuento <- totalCompra * 0.15
    Sino
        descuento <- totalCompra * 0.20
    FinSi
	
    totalPagar <- totalCompra - descuento
	
    Escribir "El dinero descontado es: $", descuento
    Escribir "El total a pagar es: $", totalPagar
	
FinAlgoritmo