# 1. Crear una lista y acceder a sus elementos
paises = ["México", "Argentina", "España", "Colombia", "Perú"]
print("Tercer país de la lista:", paises[2])

# 2. Modificar elementos de una lista
colores = ["Rojo", "Azul", "Verde", "Amarillo"]
colores[1] = "Negro"
print("Lista de colores actualizada:", colores)

# 3. Agregar elementos a una lista
frutas = []
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Naranja")
print("Lista de frutas:", frutas)

# 4. Insertar elementos en una posición específica
numeros = [10, 20, 30]
numeros.insert(1, 50)
print("Lista con número insertado:", numeros)

# 5. Eliminar elementos de una lista
animales = ["Perro", "Gato", "León", "Tigre", "Elefante"]
animales.remove("León")
print("Lista de animales actualizada:", animales)

# 6. Ordenar una lista de números
numeros_desordenados = [5, 3, 8, 1, 4]
numeros_desordenados.sort()
print("Lista ordenada:", numeros_desordenados)

# 7. Revertir el orden de una lista
nombres = ["Carlos", "Ana", "Luis", "Sofía", "Pedro"]
nombres.reverse()
print("Lista de nombres invertida:", nombres)

# 8. Contar elementos en una lista
elementos = ["a", "b", "c", "a", "b", "a"]
cantidad_a = elementos.count("a")
print("Número de veces que 'a' aparece en la lista:", cantidad_a)

# 9. Combinar dos listas
lista1 = ["Juan", "María", "José"]
lista2 = ["Luisa", "Andrés", "Elena"]
lista1.extend(lista2)
print("Lista combinada:", lista1)

# 10. Usar pop() para eliminar y obtener el último elemento
ciudades = ["Lima", "Quito", "Santiago", "Bogotá"]
ultimo = ciudades.pop()
print("Última ciudad eliminada:", ultimo)
print("Lista de ciudades actualizada:", ciudades)
