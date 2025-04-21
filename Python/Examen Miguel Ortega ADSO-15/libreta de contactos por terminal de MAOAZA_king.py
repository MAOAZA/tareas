######################################### Mini Sistema: Agenda de Contactos de 👑 MAOAZA_king ☯ prototipe########################################
from datetime import datetime
import os
import json
import sys
import re

ruta_script = os.path.abspath(sys.argv[0])
directorio_script = os.path.dirname(ruta_script)
os.chdir(directorio_script)


contactos = []

def validar_fecha(fecha):
    try:
        fecha_nacimiento = datetime.strptime(fecha, "%Y-%m-%d")
        # Comprobar si la fecha es futura
        if fecha_nacimiento > datetime.now():
            print(error("  La fecha no puede ser futura"))
            return False
        # Comprobar si la persona tiene menos de 1 año
        if (datetime.now() - fecha_nacimiento).days < 365:
            print(error("  La persona debe tener al menos 1 año de edad  "))
            return False
        return True
    except ValueError:
        return False

    
def error(texto, color="34", fondo="41", negrita=True):
    codigo = "\033["
    if negrita:
        codigo += "1;"
    codigo += f"{color};{fondo}m  {texto}  \033[0m"
    return codigo

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar contacto")
    print("2. Editar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Exportar contactos a archivo")
    print("7. Importar contactos desde archivo")
    print("8. Salir")

import re

def validar_nombre(nombre):
    # Eliminar espacios al principio y al final
    nombre = nombre.strip()

    # Reemplazar múltiples espacios por un solo espacio
    nombre = re.sub(r'\s+', ' ', nombre)

    # Verificar que el nombre no tenga más de dos palabras (primer nombre + segundo nombre)
    if len(nombre.split()) > 2:
        return False
    
    # Asegurarse de que solo contenga letras y un único espacio
    return all(part.isalpha() for part in nombre.split())

def agregar_contacto():
    nombre_correcto = False
    while not nombre_correcto:
        nombre = input("Ingrese el nombre del contacto (solo el nombre, no el apellido): ").strip()

        # Eliminar múltiples espacios y permitir solo un espacio entre nombres
        nombre = re.sub(r'\s+', ' ', nombre)

        # Verificar que no tenga más de dos palabras (primer y segundo nombre)
        if len(nombre.split()) > 2:
            print(error("  Solo escribe el nombre del contacto, sin incluir el apellido. Asegúrate de que solo haya un espacio entre los nombres.  "))
            continue
        
        # Verificar si el nombre es válido (solo letras y un único espacio entre los nombres)
        if validar_nombre(nombre):
            nombre_correcto = True
        else:
            print(error("  El nombre no debe contener números ni estar vacío. Solo se permiten letras y un máximo de dos palabras.  "))
    
    # Continuar con el resto del proceso de agregar contacto...
    apellido_correcto = False
    while not apellido_correcto:
        apellido = input("Ingrese el apellido: ")
        if validar_nombre(apellido):
            apellido_correcto = True
        else:
            print(error("  El apellido no debe contener números ni estar vacío  "))

    telefono_correcto = False
    while not telefono_correcto:
        telefono = input("Ingrese el número telefónico: ")
        if telefono.isdigit():
            telefono_correcto = True
        else:
            print(error("  El número telefónico debe contener solo números  "))

    email_correcto = False
    while not email_correcto:
        email = input("Ingrese el email: ")
        if "@" in email and "." in email:
            email_correcto = True
        else:
            print(error("  El email debe contener '@' y '.'  "))

    direccion_correcta = False
    while not direccion_correcta:
        direccion = input("Ingrese la dirección: ")
        if len(direccion.strip()) > 0:
            direccion_correcta = True
        else:
            print(error("  La dirección no puede estar vacía  "))

    ciudad_correcta = False
    while not ciudad_correcta:
        ciudad = input("Ingrese la ciudad: ")
        if validar_nombre(ciudad):
            ciudad_correcta = True
        else:
            print(error("  La ciudad no debe contener números ni estar vacía  "))

    fecha_nacimiento_correcta = False
    while not fecha_nacimiento_correcta:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        if validar_fecha(fecha_nacimiento):
            fecha_nacimiento_correcta = True
        else:
            
            fecha_nacimiento_correcta = False

    contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "ciudad": ciudad,
        "fecha_nacimiento": fecha_nacimiento
    }
    contactos.append(contacto)
    print("\n✅ Contacto guardado exitosamente.\n")
    
def input_validado(mensaje, validacion, mensaje_error):
    while True:
        entrada = input(mensaje)
        if validacion(entrada):
            return entrada
        else:
            print(error(f"  {mensaje_error}  "))

def input_fecha():
    while True:
        fecha = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print(error("  Fecha inválida. Use el formato YYYY-MM-DD  "))


def editar_contacto():
    if not contactos:
        print(error("  No hay contactos para editar  "))
        return

    buscar_contacto()
    indice = input_validado("Seleccione el número del contacto a editar: ", 
                            lambda x: x.isdigit() and 0 <= int(x) < len(contactos), 
                            "Índice inválido")
    indice = int(indice)

    while True:
        print("\n¿Qué desea editar?")
        print("1. Nombre\n2. Apellido\n3. Teléfono\n4. Email\n5. Dirección\n6. Ciudad\n7. Fecha de nacimiento\n8. Terminar edición")
        opcion_edicion = input("Seleccione una opción: ")

        if opcion_edicion == "1":
            contactos[indice]["nombre"] = input_validado("Nuevo nombre: ", validar_nombre, "Nombre inválido")
        elif opcion_edicion == "2":
            contactos[indice]["apellido"] = input_validado("Nuevo apellido: ", validar_nombre, "Apellido inválido")
        elif opcion_edicion == "3":
            contactos[indice]["telefono"] = input_validado("Nuevo teléfono: ", lambda x: x.isdigit(), "Teléfono inválido")
        elif opcion_edicion == "4":
            contactos[indice]["email"] = input_validado("Nuevo email: ", lambda x: "@" in x and "." in x, "Email inválido")
        elif opcion_edicion == "5":
            contactos[indice]["direccion"] = input("Nueva dirección: ")
        elif opcion_edicion == "6":
            contactos[indice]["ciudad"] = input_validado("Nueva ciudad: ", lambda x: x.isalpha(), "Ciudad inválida")
        elif opcion_edicion == "7":
            # Aquí es donde corregimos el proceso de edición de la fecha
            while True:
                nueva_fecha = input_fecha()  # Usamos la función input_fecha() para pedir una fecha válida
                try:
                    # Validamos que la fecha no sea futura
                    fecha_nacimiento = datetime.strptime(nueva_fecha, "%Y-%m-%d")
                    if fecha_nacimiento > datetime.now():
                        print(error("  La fecha de nacimiento no puede ser futura."))
                    else:
                        contactos[indice]["fecha_nacimiento"] = nueva_fecha
                        break  # Si la fecha es válida, salimos del bucle
                except ValueError:
                    print(error("  Fecha inválida. Use el formato YYYY-MM-DD."))
        elif opcion_edicion == "8":
            print("🔁 Edición terminada.")
            break
        else:
            print(error("  Opción inválida  "))

def eliminar_contacto():
    if not contactos:
        print(error("  No hay contactos para eliminar  "))
        return
    buscar_contacto()
    indice = input("Seleccione el número del contacto a eliminar: ")
    if indice.isdigit() and 0 <= int(indice) < len(contactos):
        confirmacion = input("¿Está seguro? (s/n): ")
        if confirmacion.lower() == "s":
            del contactos[int(indice)]
            print("✅ Contacto eliminado.")
        else:
            print("❌ Eliminación cancelada.")
    else:
        print(error("  Índice inválido  "))

def buscar_contacto():
    if not contactos:
        print(error("  No hay contactos para buscar  "))
        return

    busqueda = input("Buscar por nombre o apellido: ").lower()
    encontrados = [(i, c) for i, c in enumerate(contactos) if busqueda in c["nombre"].lower() or busqueda in c["apellido"].lower()]
    if encontrados:
        print("\nResultados encontrados:")
        for i, c in encontrados:
            print(f"{i}. {c['nombre']} {c['apellido']} - {c['telefono']}")
    else:
        print(error("  No se encontraron coincidencias  "))


def mostrar_contactos():
    if not contactos:
        print(error("  No hay contactos para mostrar  "))
        return

    def truncar(texto, largo):
        return texto if len(texto) <= largo else texto[:largo - 3] + "..."

    tipo_mostrar = input("¿Desea mostrar (1) información relevante o (2) toda la información? ")
    if tipo_mostrar == "1":
        print("\n{:<25} {:<15}".format("Nombre completo", "Teléfono"))
        print("-" * 39)
        for c in contactos:
            nombre_completo = truncar(f"{c['nombre']} {c['apellido']}", 25)
            telefono = truncar(c["telefono"], 15)
            print("{:<25} {:<15}".format(nombre_completo, telefono))
    elif tipo_mostrar == "2":
        print("\n{:<25} {:<15} {:<23} {:<30} {:<20} {:<15}".format(
            "Nombre completo", "Teléfono", "Email", "Dirección", "Ciudad", "Nacimiento"))
        print("-" * 135)
        for c in contactos:
            nombre_completo = truncar(f"{c['nombre']} {c['apellido']}", 25)
            telefono = truncar(c["telefono"], 15)
            email = truncar(c["email"], 23)
            direccion = truncar(c["direccion"], 30)
            ciudad = truncar(c["ciudad"], 20)
            nacimiento = truncar(c["fecha_nacimiento"], 15)
            print("{:<25} {:<15} {:<23} {:<30} {:<20} {:<15}".format(
                nombre_completo, telefono, email, direccion, ciudad, nacimiento))
    else:
        print(error("  Opción inválida  "))




def exportar_contactos():
    formato = input("¿En qué formato desea exportar? (1) .txt (2) .json: ")
    if formato == "1":
        nombre_archivo = input("Nombre del archivo (sin extensión): ") + ".txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for c in contactos:
                linea = "|".join([c[k] for k in ["nombre", "apellido", "telefono", "email", "direccion", "ciudad", "fecha_nacimiento"]]) + "\n"
                f.write(linea)
    elif formato == "2":
        nombre_archivo = input("Nombre del archivo (sin extensión): ") + ".json"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(contactos, f, ensure_ascii=False, indent=4)
    else:
        print(error("  Formato no válido. Exportación cancelada.  "))
        return
    print(f"📁 Contactos exportados correctamente a {nombre_archivo}")


def importar_contactos():
    def es_contacto_igual(c1, c2):
        return all(c1[k] == c2[k] for k in c1)

    def existe_contacto(contacto):
        return any(es_contacto_igual(contacto, c) for c in contactos)

    def generar_apellido_unico(nombre, apellido_base):
        sufijo = 1
        nuevo_apellido = apellido_base + str(sufijo)
        nombres_existentes = [(c["nombre"].lower(), c["apellido"].lower()) for c in contactos]
        while (nombre.lower(), nuevo_apellido.lower()) in nombres_existentes:
            sufijo += 1
            nuevo_apellido = apellido_base + str(sufijo)
        return nuevo_apellido

    archivos = [f for f in os.listdir() if f.endswith((".txt", ".json"))]
    if not archivos:
        print(error("  No hay archivos compatibles en el directorio actual  "))
        return

    print("\nArchivos disponibles para importar:\n")
    for i, archivo in enumerate(archivos):
        print(f"{i + 1}. {archivo}")
    print("0. Cancelar\n")

    seleccion = input("Seleccione el número del archivo a importar: ")
    if not seleccion.isdigit() or not (0 <= int(seleccion) <= len(archivos)):
        print(error("  Selección inválida  "))
        return

    seleccion = int(seleccion)
    if seleccion == 0:
        print("❌ Importación cancelada.\n")
        return

    archivo_elegido = archivos[seleccion - 1]
    nuevos_contactos = []

    if archivo_elegido.endswith(".txt"):
        with open(archivo_elegido, "r", encoding="utf-8") as f:
            for linea in f:
                for sep in [",", ";", "\t", ":"]:
                    if sep in linea and "|" not in linea:
                        linea = linea.replace(sep, "|")
                        break
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    contacto = {
                        "nombre": datos[0],
                        "apellido": datos[1],
                        "telefono": datos[2],
                        "email": datos[3],
                        "direccion": datos[4],
                        "ciudad": datos[5],
                        "fecha_nacimiento": datos[6]
                    }
                    nuevos_contactos.append(contacto)
    elif archivo_elegido.endswith(".json"):
        with open(archivo_elegido, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                nuevos_contactos.extend(data)

    # INICIAMOS EL CONTADOR AQUÍ
    importados = 0  # Iniciar contador de contactos importados

    for nuevo in nuevos_contactos:
        # Verificar si el contacto ya existe por nombre + teléfono
        if existe_contacto(nuevo):
            continue
        
        # Detectar duplicados por nombre/apellido pero diferente teléfono
        duplicados = [c for c in contactos if c["nombre"].lower() == nuevo["nombre"].lower()
                      and c["apellido"].lower() == nuevo["apellido"].lower()
                      and c["telefono"] != nuevo["telefono"]]
        
        if duplicados:
            # Generar nuevo apellido para evitar duplicado de nombre/apellido
            nuevo["apellido"] = generar_apellido_unico(nuevo["nombre"], nuevo["apellido"])

            # ✅ VERIFICACIÓN EXTRA: ¿ya existe contacto con ese nuevo nombre + nuevo teléfono?
            if any(c["nombre"].lower() == nuevo["nombre"].lower() and c["telefono"] == nuevo["telefono"] for c in contactos):
                print(f"⚠️ El contacto {nuevo['nombre']} {nuevo['apellido']} con el número {nuevo['telefono']} ya existe. Así que este contacto no se importará.")
                continue  # ❌ Si ya existe ese "renombrado", lo ignoramos también

        # Añadir el contacto al sistema
        contactos.append(nuevo)
        importados += 1  # Aumentamos el contador de importados

    print(f"📥 {importados} contacto(s) importado(s) desde {archivo_elegido}\n")




print("Bienvenido a la Agenda de Contactos de 👑 MAOAZA_king ☯")

fin_programa = False
primera_vez = True

while not fin_programa:
    if primera_vez:
        mostrar_menu()
        primera_vez = False
    else:
        print("\n¿Desea ver el menú principal o salir?")
        print("1. Mostrar menú")
        print("2. Salir")
        eleccion = input("Seleccione una opción: ")
        if eleccion == "1":
            mostrar_menu()
        elif eleccion == "2":
            print("\033[1;35m╔════════════════════════════════════════╗\033[0m")
            print("\033[1;35m│    \033[1;33m G r a c i a s   p o r   u s a r\033[1;35m    │\033[0m")
            print("\033[1;35m│\033[1;36m A g e n d a   d e   C o n t a c t o s \033[1;35m │\033[0m")
            print("\033[1;35m│       \033[1;33m👑 \033[1;31mM A O A Z A _ k i n g \033[0m☯\033[1;35m       │\033[0m")
            print("\033[1;35m╚════════════════════════════════════════╝\033[0m")
            print("\033[1;32m        ¡ H a s t a   l u e g o ! \033[0m🍀\n")
            break
        else:
            print(error("  Opción inválida  "))
            continue

    opcion = input("\nSeleccione una opción del menú: \n")
    if not (opcion.isdigit() and 1 <= int(opcion) <= 8):
        print(error("  Debe ingresar un número válido entre 1 y 8  "))
        continue

    opcion = int(opcion)
    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        editar_contacto()
    elif opcion == 3:
        eliminar_contacto()
    elif opcion == 4:
        buscar_contacto()
    elif opcion == 5:
        mostrar_contactos()
    elif opcion == 6:
        exportar_contactos()
    elif opcion == 7:
        importar_contactos()
    elif opcion == 8:
        fin_programa = True
        print("\033[1;35m╔════════════════════════════════════════╗\033[0m")
        print("\033[1;35m│    \033[1;33m G r a c i a s   p o r   u s a r\033[1;35m    │\033[0m")
        print("\033[1;35m│\033[1;36m A g e n d a   d e   C o n t a c t o s \033[1;35m │\033[0m")
        print("\033[1;35m│       \033[1;33m👑 \033[1;31mM A O A Z A _ k i n g \033[0m☯\033[1;35m       │\033[0m")
        print("\033[1;35m╚════════════════════════════════════════╝\033[0m")
        print("\033[1;32m        ¡ H a s t a   l u e g o ! \033[0m🍀\n")