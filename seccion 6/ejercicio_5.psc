Algoritmo ejercicio_5
		Definir monto, cuota Como Real
		
		Escribir "Ingrese el monto de la fianza:"
		Leer monto
		Si monto < 50000 Entonces
			cuota <- monto * 0.03
		SiNo
			cuota <- monto * 0.02
		FinSi
		Escribir "El monto de la fianza es: $", monto
		Escribir "La cuota que el cliente debe pagar es: $", cuota
		
FinAlgoritmo
	
