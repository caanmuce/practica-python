# Ejercicios de Python y PSeInt

## Práctica para la competencia de algoritmos en tecnología

Repositorio académico dedicado al aprendizaje progresivo de **lógica de programación**, **algoritmos**, **Python** y **Programación Orientada a Objetos (POO)**. Contiene ejercicios de consola y algoritmos en PSeInt que permiten practicar desde operaciones básicas hasta validaciones, ciclos, menús interactivos, acumuladores, herencia y polimorfismo.

> Una colección de ejercicios para pensar paso a paso, transformar problemas en algoritmos y fortalecer las bases necesarias para competir en programación.

## Contenido

- [Objetivos](#objetivos)
- [Ruta de aprendizaje](#ruta-de-aprendizaje)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Temas practicados](#temas-practicados)
- [Requisitos](#requisitos)
- [Cómo ejecutar los ejercicios](#cómo-ejecutar-los-ejercicios)
- [Ejemplos de ejecución](#ejemplos-de-ejecución)
- [Estado del proyecto](#estado-del-proyecto)

## Objetivos

- Desarrollar el razonamiento lógico y la resolución de problemas.
- Representar soluciones mediante algoritmos y pseudocódigo.
- Practicar entradas, salidas, variables, operadores y estructuras de control.
- Construir soluciones con ciclos, contadores, acumuladores y validaciones.
- Aplicar conceptos fundamentales de POO en situaciones cotidianas.
- Preparar una base sólida para la competencia de algoritmos en tecnología.

## Ruta de aprendizaje

El repositorio está organizado como una progresión de dificultad:

| Sección | Enfoque | Cantidad |
|---|---|---:|
| `ejercicios seccion 9` | Fundamentos de Python, operaciones y decisiones | 5 ejercicios |
| `seccion 6` | Algoritmos y toma de decisiones en PSeInt | 10 algoritmos |
| `seccion 12` | Ciclos, acumuladores, promedios y factoriales | 8 ejercicios |
| `seccion11` | Validaciones, menús, estadísticas y simulaciones | 10 ejercicios |
| `POO/seccion 3 (1)` | Clases, objetos, atributos y métodos | 7 ejercicios |
| `POO/seccion 4 (1)` | Encapsulamiento, herencia y polimorfismo | 11 ejercicios |

## Estructura del repositorio

```text
.
├── ejercicios seccion 9/
│   ├── ejercicio1.py       # Saludo y entrada de texto
│   ├── ejercicio2.py       # Suma de dos números
│   ├── ejercicio3.py       # Mayoría de edad
│   ├── ejercicio4.py       # Promedio de notas
│   └── ejercicio5.py       # Operaciones aritméticas
├── seccion 6/
│   └── *.psc               # Algoritmos de decisiones en PSeInt
├── seccion11/
│   └── ejercicio1.py ... ejercicio10.py
├── seccion 12/
│   └── ejercicio1.py ... ejercicio8.py
└── POO/
    ├── seccion 3 (1)/      # Modelado inicial con clases
    └── seccion 4 (1)/      # Herencia y polimorfismo
```

## Temas practicados

### Python y lógica procedural

- Variables y tipos de datos: `str`, `int` y `float`.
- Entrada y salida por consola con `input()` y `print()`.
- Operadores aritméticos, relacionales y lógicos.
- Condicionales `if`, `elif` y `else`.
- Ciclos `for` y `while`.
- Contadores y acumuladores.
- Cálculo de promedios, máximos y mínimos.
- Listas para almacenar notas y temperaturas.
- Validación de rangos y entradas con `try/except`.
- Menús interactivos y simulaciones sencillas.

### PSeInt

Los algoritmos de la `seccion 6` practican:

- Declaración de variables con `Definir`.
- Lectura y escritura con `Leer` y `Escribir`.
- Decisiones con `Si`, `Sino` y `FinSi`.
- Cálculos financieros, descuentos, cuotas e inversiones.
- Traducción de problemas cotidianos a pseudocódigo.

### Programación Orientada a Objetos

- Definición de clases y creación de objetos.
- Constructores mediante `__init__`.
- Atributos y métodos.
- Validación del estado de los objetos.
- Encapsulamiento convencional con atributos como `_precio`, `_stock` y `_salario`.
- Herencia y reutilización con `super()`.
- Sobrescritura de métodos.
- Polimorfismo aplicado a vehículos, animales, empleados y productos.

## Requisitos

- [Python 3](https://www.python.org/downloads/)
- [PSeInt](https://pseint.sourceforge.net/) para ejecutar los archivos `.psc` (opcional)
- Una terminal o editor de código, como Visual Studio Code

El repositorio no requiere paquetes externos ni archivos de configuración adicionales. Cada ejercicio funciona como un script independiente.

## Cómo ejecutar los ejercicios

Desde la carpeta raíz del repositorio, ejecuta un archivo Python con:

```bash
python "ruta/al/ejercicio.py"
```

En algunos sistemas puede ser necesario utilizar `python3`:

```bash
python3 "ruta/al/ejercicio.py"
```

Los nombres de algunas carpetas contienen espacios, por lo que se recomienda conservar las comillas en la ruta.

Para ejecutar un ejercicio específico:

```bash
python "seccion11/ejercicio5.py"
python "POO/seccion 4 (1)/EJERCICIO8.py"
python "ejercicios seccion 9/ejercicio4.py"
```

Los programas solicitan datos durante la ejecución. Sigue las instrucciones que aparecen en la consola.

### Ejecutar algoritmos PSeInt

1. Abre PSeInt.
2. Selecciona **Abrir** y elige un archivo de la carpeta `seccion 6`.
3. Ejecuta el algoritmo y proporciona los datos solicitados.

## Ejemplos de ejercicios

- **Fundamentos:** saludo, suma, mayoría de edad, promedio y operaciones aritméticas.
- **Ciclos:** tablas de multiplicar, cuenta regresiva, números pares y factorial.
- **Validaciones:** contraseñas, calificaciones, edades, stock e intentos limitados.
- **Análisis de datos:** ventas, temperaturas, números positivos y negativos.
- **Simulaciones:** inventario y ascensor.
- **POO:** cuentas bancarias, productos, libros, aprendices, vehículos, mascotas, animales y empleados.
- **PSeInt:** vivienda, jubilación, descuentos, inversión, reforestación y sistema SAR.

## Estado del proyecto

Este repositorio se encuentra en construcción como material de práctica y aprendizaje. Actualmente contiene:

- 41 ejercicios en Python.
- 10 algoritmos en PSeInt.
- Scripts independientes orientados a la consola.
- Ejemplos de lógica procedural y POO.

No incluye todavía una suite de pruebas automatizadas, persistencia de datos, bases de datos ni una aplicación integrada. Las soluciones están pensadas para estudiar, experimentar y mejorar progresivamente.

Algunos nombres de archivo conservan su forma original, como `ejercio3.py` y `EJERCICIO8.py`, para mantener la correspondencia con las actividades entregadas.

## Propósito académico

Este proyecto forma parte del proceso de preparación para la **competencia de algoritmos en la tecnología**. La práctica constante de estos ejercicios ayuda a mejorar la lectura de problemas, el diseño de soluciones, la implementación y la validación de resultados.

> Cada algoritmo resuelto es una oportunidad para convertir una idea en una solución funcional.
