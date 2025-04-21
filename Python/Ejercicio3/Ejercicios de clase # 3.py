##############################################    Ejercicio # 1    ##############################################
print("#####################    Ejercicio # 1    #####################")
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá"
}
print("Nombre de la persona:", persona["nombre"])

##############################################    Ejercicio # 2    ##############################################
print("#####################    Ejercicio # 2    #####################")
estudiante = {
    "nombre": "Ana",
    "calificacion": 8.0
}
# Agregar una nueva clave
estudiante["materia"] = "Matemáticas"
# Modificar la calificación
estudiante["calificacion"] = 9.5
print("Información del estudiante actualizada:", estudiante)

##############################################    Ejercicio # 3    ##############################################
print("#####################    Ejercicio # 3    #####################")
pelicula = {
    'titulo': 'Inception',
    'director': 'Christopher Nolan',
    'año': 2010
}
print("Diccionario original:", pelicula)
del pelicula['director']
print("Diccionario actualizado:", pelicula)

##############################################    Ejercicio # 4    ##############################################
print("#####################    Ejercicio # 4    #####################")
paises_capitales = {
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma',
    'Alemania': 'Berlín'
}
for pais, capital in paises_capitales.items():
    print(f"El país es {pais} y su capital es {capital}")

##############################################    Ejercicio # 5    ##############################################
print("#####################    Ejercicio # 5    #####################")
productos = {
    'manzana': 1.2,
    'banana': 0.8,
    'naranja': 1.5
}
stock = productos.get('pera', 'No disponible')
print(f"El stock de pera es: {stock}")

##############################################    FIN    ##############################################