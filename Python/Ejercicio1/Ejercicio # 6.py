######################################## EJERCICIO # 6 ########################################
saldo = -1
valorRetirar = -1
while saldo <= 0:
    saldo = int(input("Escribe el saldo de tu cuenta sin incluir decimales: "))
    if saldo < 0:
        print ("Usted no puede tener un saldo negativo, vuelva a intentar")

while valorRetirar <= 0:
    valorRetirar = int(input("Escribe la cantidad que deseas retirar: "))
    if valorRetirar < 0:
       print ("Usted no puede retirar un valor negativo")
print ("Retiro aprobado")
print ("")
print ("")
print ("Generando RECIBO DE SU RETIRO")
print ("")
print ("")
print ("")
print ("")
print ("")
print ("__________RECIBO DE RETIRO__________")
print ("Saldo antes de retirar = ", saldo)
print ("Cantidad a retirar     = ", valorRetirar)
saldo = saldo - valorRetirar
print ("Nuevo saldo            = ", saldo)
print ("")
print ("")
print ("Ya puede sacar su dinero de la maquina en la ventanilla")