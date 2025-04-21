#################### Ejercicio # 1 ####################
def ejercicio_1():
    ejercicio_finalizado = False
    print("Ejercicio # 1")
    print("")
    while not ejercicio_finalizado:
        try:
            a = float(input("   Ingresa el primer número: "))
            b = float(input("   Ingresa el segundo número: "))
            resultado = a / b
            print("   Resultado:", resultado)
            ejercicio_finalizado = True
        except ZeroDivisionError:
            print("   Error: No se puede dividir entre 0.")
        except ValueError:
            print("   Error: Debes ingresar un número válido.")

#################### Ejercicio # 2 ####################
def ejercicio_2():
    ejercicio_finalizado = False
    print("Ejercicio # 2")
    print("")
    while not ejercicio_finalizado:
        lista = [10, 20, 30, 40, 50]
        indice_str = input("2. Ingresa un índice (0-4): ")
        if not indice_str.isdigit():
            print("   Error: Debes ingresar un número entero.")
            continue
        indice = int(indice_str)
        if indice < 0 or indice >= len(lista):
            print("   Error: Índice fuera de rango.")
            continue
        print("   Valor en el índice:", lista[indice])
        ejercicio_finalizado = True

#################### Ejercicio # 3 ####################
def ejercicio_3():
    ejercicio_finalizado = False
    print("Ejercicio # 3")
    print("")
    while not ejercicio_finalizado:
        try:
            num = int(input("3. Ingresa un número: "))
            print("   Número convertido:", num)
            ejercicio_finalizado = True
        except ValueError:
            print("   Error: Ingresa un número válido.")

#################### Ejercicio # 4 ####################
def ejercicio_4():
    ejercicio_finalizado = False
    print("Ejercicio # 4")
    print("")
    while not ejercicio_finalizado:
        try:
            nombre = input("4. Ingresa el nombre del archivo a abrir: ")
            with open(nombre, "r") as f:
                print("   Contenido del archivo:\n", f.read())
            ejercicio_finalizado = True
        except FileNotFoundError:
            print("   Error: El archivo no existe.")

#################### Ejercicio # 5 ####################
def ejercicio_5():
    ejercicio_finalizado = False
    print("Ejercicio # 5")
    print("")
    while not ejercicio_finalizado:
        try:
            a = float(input("5. Ingresa el primer número: "))
            b = float(input("   Ingresa el segundo número: "))
            op = input("   Ingresa operación (+, -, *, /): ")
            if op == "+":
                print("   Resultado:", a + b)
            elif op == "-":
                print("   Resultado:", a - b)
            elif op == "*":
                print("   Resultado:", a * b)
            elif op == "/":
                print("   Resultado:", a / b)
            else:
                print("   Operación inválida.")
                continue
            ejercicio_finalizado = True
        except ZeroDivisionError:
            print("   Error: División por cero.")
        except ValueError:
            print("   Error: Ingresa números válidos.")

#################### Ejercicio # 6 ####################
def ejercicio_6():
    ejercicio_finalizado = False
    print("Ejercicio # 6")
    print("")
    productos = {"A001": 10.99, "B002": 5.49, "C003": 7.75}
    while not ejercicio_finalizado:
        codigo = input("6. Ingresa código de producto: ")
        try:
            print("   Precio: $", productos[codigo])
            ejercicio_finalizado = True
        except KeyError:
            print("   Error: Código no encontrado.")

#################### Ejercicio # 7 ####################
def ejercicio_7():
    ejercicio_finalizado = False
    print("Ejercicio # 7")
    print("")
    usuarios = {"admin": "1234", "juan": "abcd", "ana": "qwerty"}
    while not ejercicio_finalizado:
        user = input("7. Usuario: ")
        pwd = input("   Contraseña: ")
        try:
            if usuarios[user] == pwd:
                print("   Acceso concedido.")
                ejercicio_finalizado = True
            else:
                print("   Contraseña incorrecta.")
        except KeyError:
            print("   Usuario no existe.")

def ejercicio_8():
    ejercicio_finalizado = False
    print("Ejercicio # 8")
    print("")
    while not ejercicio_finalizado:
        try:
            entrada = input("8. Ingresa números separados por coma: ")
            
            # Verificamos si hay caracteres no permitidos
            for c in entrada:
                if not (c.isdigit() or c == ',' or c.isspace()):
                    raise Exception("   Error: No uses caracteres especiales. Solo se permiten números, comas y espacios.")

            lista = entrada.split(",")
            suma = sum(int(num.strip()) for num in lista)
            print("   Suma total:", suma)
            ejercicio_finalizado = True

        except ValueError:
            print("   Error: Todos los valores deben ser números enteros.")
        except Exception as e:
            print(e)

#################### Ejercicio # 9 ####################
def ejercicio_9():
    ejercicio_finalizado = False
    print("Ejercicio # 9")
    print("")
    while not ejercicio_finalizado:
        try:
            print("9. Ingresa la primera matriz 2x2:")
            matriz1 = [[int(input(f"   Elemento [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
            print("   Ingresa la segunda matriz 2x2:")
            matriz2 = [[int(input(f"   Elemento [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
            suma = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]
            print("   Matriz resultante:")
            for fila in suma:
                print("  ", fila)
            ejercicio_finalizado = True
        except ValueError:
            print("   Error: Solo se permiten números.")

#################### Ejercicio # 10 ####################
def ejercicio_10():
    import random
    import string
    ejercicio_finalizado = False
    print("Ejercicio # 10")
    print("")
    while not ejercicio_finalizado:
        n_str = input("¿Cuántos caracteres para la contraseña?: ")
        if not n_str.isdigit():
            print("   Error: Ingresa un número válido.")
            continue
        n = int(n_str)
        if n <= 0:
            print("   Error: La cantidad debe ser mayor que 0.")
            continue
        caracteres = string.ascii_letters + string.digits
        contraseña = ''.join(random.choice(caracteres) for _ in range(n))
        print("   Contraseña generada:", contraseña)
        ejercicio_finalizado = True

# Llamar los ejercicios

ejercicio_8()

