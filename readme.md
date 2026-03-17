
# Sistema de Gestión Básica de Estudiantes

## Descripción

Sistema interactivo en Python que permite registrar estudiantes, gestionar sus calificaciones y evaluar su desempeño académico.

## Características

- **Registro de estudiantes**: Captura nombre, edad y tres calificaciones con validación de datos
- **Cálculo de promedio**: Promedia automáticamente las tres notas ingresadas
- **Evaluación académica**: Clasifica el estado del estudiante (Aprobado, En recuperación, Reprobado)
- **Listado completo**: Visualiza todos los estudiantes registrados con sus promedios y estados

## Uso

```bash
python registro_estudiantes.py
```

Selecciona una opción del menú:
1. Registrar un nuevo estudiante
2. Ver listado de todos los estudiantes
3. Salir del programa

## Criterios de Evaluación

| Promedio | Estado |
|----------|--------|
| ≥ 4.0 | Aprobado |
| 3.0 - 3.9 | En recuperación |
| < 3.0 | Reprobado |

## Introducción
Este es un programa en Python que permite registrar estudiantes, calcular su promedio y determinar su estado académico (aprobado, recuperación o reprobado) mediante un menú interactivo.

---

## Estructura general
El programa está dividido en funciones, lo que permite que el código sea más organizado, fácil de entender y también más sencillo de modificar.

---

## Almacenamiento de datos
Se utiliza una lista llamada `estudiantes` donde se guardan todos los estudiantes.  
Cada estudiante se almacena como un diccionario, lo que permite acceder fácilmente a sus datos como nombre, edad y promedio.

---

## Registro de estudiante
Se solicitan nombre, edad y 3 notas con validaciones para evitar errores:

- El nombre no puede estar vacío  
- La edad debe ser mayor que 0  
- Las notas deben estar entre 0.0 y 5.0  

Se utiliza `try-except` para evitar que el programa falle si el usuario ingresa datos incorrectos.

---

## Procesamiento
El promedio se calcula en una función llamada `calcular_promedio()`.  

Luego, con la función `evaluar_estado()`, se determina si el estudiante:
- Aprueba  
- Queda en recuperación  
- Reprueba  

---

## Salida de datos
Los resultados se muestran en consola usando `print()` y f-strings, formateando los números a 2 decimales.

---

## Menú principal
Se utiliza un `while True` para permitir que el usuario interactúe con el sistema hasta que decida salir.

---

## Ejecución
El programa inicia con:

```python
if __name__ == "__main__":
    menu()

