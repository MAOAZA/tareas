# 1. Crear y acceder a elementos de un diccionario
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])  # Salida: Juan

# 2. Agregar y modificar elementos en un diccionario
estudiante = {"nombre": "Ana", "calificación": 8.5}
estudiante["materia"] = "Matemáticas"
estudiante["calificación"] = 9.5
print(estudiante)  # Salida: {'nombre': 'Ana', 'calificación': 9.5, 'materia': 'Matemáticas'}

# 3. Eliminar elementos de un diccionario
pelicula = {"titulo": "Inception", "director": "Christopher Nolan", "año": 2010}
del pelicula["director"]
print(pelicula)  # Salida: {'titulo': 'Inception', 'año': 2010}

# 4. Recorrer un diccionario con un bucle for
paises = {"España": "Madrid", "Francia": "París", "Italia": "Roma"}
for pais, capital in paises.items():
    print(f"{pais} - {capital}")

# 5. Usar get() para obtener valores de forma segura
producto = {"nombre": "Laptop", "precio": 1200}
stock = producto.get("stock", "No disponible")
print(stock)  # Salida: No disponible
