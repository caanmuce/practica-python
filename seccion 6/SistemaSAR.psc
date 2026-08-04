Algoritmo SistemaSAR
	Definir salario, aporte_empresa, aporte_trabajador, total_SAR, pago_final Como Real
    Definir opcion Como Entero
	
    Escribir "Ingrese el salario del trabajador:"
    Leer salario
	
    Escribir "Ingrese el porcentaje que aporta la empresa (ej: 0.05 para 5%):"
    Leer aporte_empresa
	
    Escribir "¿Como desea aportar?"
    Escribir "1. Cuota fija"
    Escribir "2. Porcentaje del salario"
    Leer opcion
	
    Si opcion = 1 Entonces
        Escribir "Ingrese la cuota fija:"
        Leer aporte_trabajador  
    Sino
        Escribir "Ingrese el porcentaje (ej: 0.03 para 3%):"
        Leer aporte_trabajador
        aporte_trabajador <- salario * aporte_trabajador
    FinSi
	
    aporte_empresa <- salario * aporte_empresa
    total_SAR <- aporte_empresa + aporte_trabajador
    pago_final <- salario - aporte_trabajador
	
    Escribir "Total depositado al SAR: ", total_SAR
    Escribir "Pago mensual del trabajador: ", pago_final
FinAlgoritmo
