# =============================================
#   SISTEMA DE GESTIÓN BÁSICA DE ESTUDIANTES
# =============================================
 
estudiantes = []
 
 
def registrar_estudiante():
    """Solicita y retorna los datos de un estudiante con validaciones."""
    print("\n--- Registro de estudiante ---")
 
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del estudiante: ").strip()
 
    edad = None
    while edad is None:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser mayor que 0.")
                edad = None
        except ValueError:
            print("Por favor ingrese un número entero válido.")
 
    notas = []
    for i in range(1, 4):
        nota = None
        while nota is None:
            try:
                nota = float(input(f"Ingrese la nota {i} (0.0 a 5.0): "))
                if nota < 0 or nota > 5:
                    print("La nota debe estar entre 0.0 y 5.0.")
                    nota = None
            except ValueError:
                print("Por favor ingrese un número válido.")
        notas.append(nota)
 
    return {
        "nombre": nombre,
        "edad": edad,
        "nota1": notas[0],
        "nota2": notas[1],
        "nota3": notas[2],
    }
 
 
def calcular_promedio(n1, n2, n3):
    """Calcula y retorna el promedio de tres notas."""
    return (n1 + n2 + n3) / 3
 
 
def evaluar_estado(promedio):
    """Determina y retorna el estado académico según el promedio."""
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"
 
 
def mostrar_resultado(datos):
    """Muestra el resultado detallado de un estudiante recién registrado."""
    print("\n===== RESULTADO DEL ESTUDIANTE =====")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']} años")
    print(f"Nota 1: {datos['nota1']:.2f}")
    print(f"Nota 2: {datos['nota2']:.2f}")
    print(f"Nota 3: {datos['nota3']:.2f}")
    print(f"Promedio: {datos['promedio']:.2f}")
    print(f"Estado académico: {datos['estado']}")
 
 
def mostrar_listado():
    """Muestra el listado numerado de todos los estudiantes registrados."""
    print("\n===== LISTADO DE ESTUDIANTES =====")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for i, e in enumerate(estudiantes, start=1):
        print(f"{i}. {e['nombre']} - Edad: {e['edad']} - Promedio: {e['promedio']:.2f} - Estado: {e['estado']}")
 
 
def menu():
    """Menú principal del sistema."""
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
        print("1. Registrar estudiante")
        print("2. Mostrar todos los estudiantes")
        print("3. Salir")
 
        opcion = input("Seleccione una opción: ").strip()
 
        if opcion == "1":
            datos = registrar_estudiante()
            promedio = calcular_promedio(datos["nota1"], datos["nota2"], datos["nota3"])
            estado = evaluar_estado(promedio)
            datos["promedio"] = promedio
            datos["estado"] = estado
            estudiantes.append(datos)
            mostrar_resultado(datos)
 
        elif opcion == "2":
            mostrar_listado()
 
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
 
        else:
            print("Opción no válida. Por favor ingrese 1, 2 o 3.")
 
 
# Punto de entrada del programa
if __name__ == "__main__":
    menu()
    