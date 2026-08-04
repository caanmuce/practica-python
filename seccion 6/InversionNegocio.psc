Algoritmo InversionNegocio
	Definir inversion_total, hipoteca, inversion_persona, inversion_socio, restante Como Real
	
    Escribir "Ingrese la inversion total:"
    Leer inversion_total
	
    Escribir "Ingrese el monto de la hipoteca:"
    Leer hipoteca
	
    Si hipoteca < 1000000 Entonces
        inversion_persona <- inversion_total * 0.50
        inversion_socio <- inversion_total * 0.50
    Sino
        inversion_persona <- hipoteca
        restante <- inversion_total - hipoteca
        inversion_persona <- inversion_persona + (restante / 2)
        inversion_socio <- restante / 2
    FinSi
	
    Escribir "Inversion de la persona: ", inversion_persona
    Escribir "Inversion del socio: ", inversion_socio
FinAlgoritmo
