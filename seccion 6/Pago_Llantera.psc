Algoritmo Pago_Llantera
	
    Definir cantidad Como Entero
    Definir precio, total Como Real
	
    Escribir "Ingrese la cantidad de llantas que desea comprar:"
    Leer cantidad
	
    Si cantidad < 5 Entonces
        precio <- 800
    Sino
        precio <- 700
    FinSi
	
    total <- cantidad * precio
	
    Escribir "El precio por cada llanta es: $", precio
    Escribir "El total a pagar es: $", total
	
FinAlgoritmo
