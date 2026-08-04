Algoritmo Clasificacion_Jubilacion_1997
	
    Definir edad, antiguedad Como Entero
    Definir tipo Como Cadena
	
    Escribir "CLASIFICACION DE JUBILACION IMSS 1997"
    
    Escribir "Ingrese la edad de la persona: "
    Leer edad
    
    Escribir "Ingrese la antiguedad en su empleo: "
    Leer antiguedad
	
    Si edad >= 60 Y antiguedad < 25 Entonces
        tipo <- "jubilacion por edad "
        
    Sino
        Si edad < 60 Y antiguedad >= 25 Entonces
            tipo <- "Jubilacion por antiguedad joven"
            
        Sino
            Si edad >= 60 Y antiguedad >= 25 Entonces
                tipo <- "Jubilacion por antiguedad adulta"
            Sino
                tipo <- "No cumle con los requisitos"
            FinSi
        FinSi
    FinSi
	
    Escribir "Tipo de jubilacion asignada: ", tipo
	
FinAlgoritmo