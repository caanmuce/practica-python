Algoritmo ejercicio_4
	definir sexo, edad Como entero;
	definir num_pulsaciones Como real;
	
	
	escribir "ingrese su numero de pulsaciones"
	leer num_pulsaciones;
	escribir "ingrese su edad"
	leer edad;
	escribir "elija su sexo"
	escribir "1. hombre"
	escribir "2. mujer"
	leer sexo;
	
	Si sexo == 1 Entonces
        num_pulsaciones <- (220 - edad) / 10
        Escribir "Para una mujer de ", edad, " años:"
    Sino
        Si sexo == 2 Entonces
            num_pulsaciones <- (210 - edad) / 10
            Escribir "Para un hombre de ", edad, " años:"
        Sino
            Escribir "Opción de sexo no válida."
            num_pulsaciones <- 0
        FinSi
    FinSi
    
    Si num_pulsaciones > 0 Entonces
        Escribir "El número de pulsaciones por cada 10 segundos es: ", num_pulsaciones
    FinSi
	
FinAlgoritmo
