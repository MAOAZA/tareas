######################################## EJERCICIO # 4 ########################################

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Verificar cuál es el mayor número
if numero1 > numero2:
    print(f"El número mayor es {numero1}.")
elif numero2 > numero1:
    print(f"El número mayor es {numero2}.")
else:
    print("Ambos números son iguales.")