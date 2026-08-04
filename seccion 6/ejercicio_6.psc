Algoritmo ejercicio_6
		Definir materias Como Entero
		Definir costo_materia, promedio, subtotal, total Como Real
		
		Escribir "Ingrese el número de materias que cursa:"
		Leer materias
		
		Escribir "Ingrese el costo de cada materia:"
		Leer costo_materia
		
		Escribir "Ingrese el promedio obtenido en el último periodo:"
		Leer promedio
		
		subtotal <- materias * costo_materia
		
		Si promedio >= 9 Entonces
			total <- subtotal * 0.70
			Escribir "Aplica para beneficio: Descuento del 30% y exención de IVA."
		SiNo
			total <- subtotal * 1.10
			Escribir "No aplica para beneficio: Se incluye el 10% de IVA."
		FinSi
		
		Escribir "El total a pagar es: $", total
		
FinAlgoritmo
	
