######################################## EJERCICIO # 3 ########################################

usuario_correcto = "admin"
contraseña_correcta = "1234"

usuario = input("Ingresa tu nombre de usuario: ")
contraseña = input("Ingresa tu contraseña: ")

# Verificar si las credenciales son correctas
if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado. Credenciales incorrectas.")