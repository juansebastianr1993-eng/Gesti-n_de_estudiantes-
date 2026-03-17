
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

