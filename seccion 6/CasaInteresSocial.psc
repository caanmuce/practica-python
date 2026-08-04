Algoritmo CasaInteresSocial
	Definir ingresos, costo_casa, enganche, resto, pago_mensual Como Real
    
    Escribir "Ingrese los ingresos del comprador:"
    Leer ingresos
    
    Escribir "Ingrese el costo de la casa:"
    Leer costo_casa
	
    Si ingresos < 8000 Entonces
        enganche <- costo_casa * 0.15
        resto <- costo_casa - enganche
        pago_mensual <- resto / (10 * 12)
    Sino
        enganche <- costo_casa * 0.30
        resto <- costo_casa - enganche
        pago_mensual <- resto / (7 * 12)
    FinSi
	
    Escribir "El enganche es: ", enganche
    Escribir "El pago mensual es: ", pago_mensual

FinAlgoritmo
