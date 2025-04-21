for i in range(6):
    print(i)
    i = i+1

print(i)
print(" ")


##############################################    Ejercicio # 1    ##############################################
print("#####################    Ejercicio # 1    #####################")
lista_paises = ['Colombia', 'Venezuela', 'Estados Unidos', 'Francia', 'Espana']
print(lista_paises[3])
print(" ")


##############################################    Ejercicio # 2    ##############################################
print("#####################    Ejercicio # 2    #####################")
lista_colores = ['Amarillo', 'Azul', 'Rojo', 'Verde']
lista_colores[2] = "Negro"
print(lista_colores[2])
print(" ")


##############################################    Ejercicio # 3    ##############################################
print("#####################    Ejercicio # 3    #####################")
lista_vacia = list()
lista_vacia.append('Manzana')
lista_vacia.append('Pera')
lista_vacia.append('Banano')
print(lista_vacia)
print(" ")


##############################################    Ejercicio # 4    ##############################################
print("#####################    Ejercicio # 4    #####################")
lista_numeros = [1, 2, 3]
lista_numeros.insert(2, 50)
print(lista_numeros)
print(" ")


##############################################    Ejercicio # 5    ##############################################
print("#####################    Ejercicio # 5    #####################")
lista_animales = ['Perro', 'Gato', 'Conejo', 'Gorila', 'Pato']
lista_animales.remove('Conejo')
print(lista_animales)
print(" ")


##############################################    Ejercicio # 6    ##############################################
print("#####################    Ejercicio # 6    #####################")
lista_numeros_desordenados = [1, 6, 4, 3, 8, 9, 2, 7, 5]
lista_numeros_desordenados.sort(reverse=None)
print(lista_numeros_desordenados)
print(" ")


##############################################    Ejercicio # 7    ##############################################
print("#####################    Ejercicio # 7    #####################")
lista_nombres = ['Isabel', 'Edwin', 'Juan', 'Felipe', 'Maria']
lista_nombres.reverse()
print(lista_nombres)
print(" ")


##############################################    Ejercicio # 8    ##############################################
print("#####################    Ejercicio # 8    #####################")
lista_con_elementos_repetidos = ['Carro', 'Llanta', 'Carro', 'Parabrisas', 'Carro', 'Carro', 'Freno', 'Exosto']
print("La palabra **Carro** aparece ", lista_con_elementos_repetidos.count('Carro') , " veces en la lista")
print(" ")


##############################################    Ejercicio # 9    ##############################################
print("#####################    Ejercicio # 9    #####################")
lista_nombre_persona_1 = ['Maria Isabel Espana']
lista_nombre_persona_2 = ['Miguel Angel Ortega']
lista_nombre_persona_1.extend(lista_nombre_persona_2)
print(lista_nombre_persona_1)
print(" ")


##############################################    Ejercicio # 10    ##############################################
print("#####################    Ejercicio # 10    #####################")
lista_ciudades = ['Cali', 'Medellin', 'Pasto', 'Palmira', 'Pereira']
ultima_ciudad = lista_ciudades.pop()
print("Esta es la lista de las ciudades sin la ultima ciudad ", lista_ciudades)
print("La ciudad que se elimino de la lista fue: " , ultima_ciudad)
print(" ")

##############################################    FIN    ##############################################