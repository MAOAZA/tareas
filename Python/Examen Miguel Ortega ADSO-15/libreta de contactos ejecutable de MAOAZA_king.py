import os
import sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import json
import tempfile
from datetime import datetime

contactos = []

def guardar_contactos():
    with open("contactos.json", "w", encoding="utf-8") as f:
        json.dump(contactos, f, ensure_ascii=False, indent=4)

def cargar_contactos():
    global contactos
    if os.path.exists("contactos.json"):
        try:
            with open("contactos.json", "r", encoding="utf-8") as f:
                contactos = json.load(f)
                # Actualizamos la vista después de cargar los contactos
                app.ver_contactos()
        except json.JSONDecodeError as e:
            print("Error al cargar el archivo JSON:", e)
            messagebox.showerror("Error", "Hubo un problema al cargar el archivo contactos.json.")
    else:
        print("No se encontró el archivo contactos.json")

def calcular_edad(fecha_nacimiento):
    try:
        fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.today()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return str(edad)
    except:
        return "N/A"

def nombre_completo_existe(nombre, apellido, indice_excluir=None):
    for i, c in enumerate(contactos):
        if i == indice_excluir:
            continue
        if c["nombre"].lower() == nombre.lower() and c["apellido"].lower() == apellido.lower():
            return True
    return False


def validar_fecha(fecha):
    try:
        f = datetime.strptime(fecha, "%Y-%m-%d")
        return f <= datetime.today()
    except:
        return False

def agregar_prefijo(apellido_base, nombre, indice_excluir=None):
    """
    Agrega un número al apellido si ya existe un contacto con el mismo nombre y apellido.
    Se excluye el contacto en el índice 'indice_excluir' para evitar duplicados consigo mismo.
    """
    sufijo = 1
    nuevo_apellido = f"{apellido_base}{sufijo}"
    
    while any(
        i != indice_excluir and 
        c["nombre"].lower() == nombre.lower() and 
        c["apellido"].lower() == nuevo_apellido.lower()
        for i, c in enumerate(contactos)
    ):
        sufijo += 1
        nuevo_apellido = f"{apellido_base}{sufijo}"

    return nuevo_apellido



def validar_datos_contacto(datos):
    if not any(c.isalpha() for c in datos["nombre"]):
        return "El nombre debe contener al menos una letra."
    if not any(c.isalpha() for c in datos["apellido"]):
        return "El apellido debe contener al menos una letra."
    if not datos["telefono"].isdigit():
        return "El teléfono debe contener solo números."
    if "@" not in datos["email"] or "." not in datos["email"]:
        return "El correo debe contener '@' y '.'."
    if not any(c.isalpha() for c in datos["direccion"]) or not any(c.isdigit() for c in datos["direccion"]):
        return "La dirección debe contener al menos una letra y un número." 
    if any(c.isdigit() for c in datos["ciudad"]):
        return "La ciudad no debe contener números."
    if not validar_fecha(datos["fecha_nacimiento"]):
        return "La fecha de nacimiento no puede ser futura o inválida."
    edad = calcular_edad(datos["fecha_nacimiento"])
    if int(edad) < 1:
        return "No puedes tener un contacto de una persona que aún no tiene 1 año de nacido."
    return None

def agregar_numero_consecutivo(nombre, telefono, email):
    """Agregar un número consecutivo si el nombre ya existe con un teléfono diferente"""
    contador = 1
    for c in contactos:
        if c['nombre'] == nombre and c['telefono'] != telefono:
            contador += 1
    return f"{nombre} ({contador})" if contador > 1 else nombre
def contacto_existe(datos, indice_excluir=None):
    """Verifica si ya existe un contacto con el mismo nombre, teléfono o correo.
    Se puede excluir un índice específico (usado al editar un contacto)."""
    for i, c in enumerate(contactos):
        # Excluir el contacto que estamos editando
        if i == indice_excluir:
            continue

        # Verificar si ya existe un contacto con el mismo nombre, teléfono o correo
        if (c['nombre'].lower() == datos['nombre'].lower() and 
            (c['telefono'] == datos['telefono'] or c['email'].lower() == datos['email'].lower())):
            return True
    return False

class LibretaContactos:
    def __init__(self, root):
        self.root = root
        self.root.title("📘 Libreta de Contactos de MAOAZA_king")
        self.root.geometry("800x550")
        self.root.minsize(800, 550)
        self.root.configure(bg="#f0f0f0")

        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("TButton", padding=6, background="#5bbcfc", foreground="black", font=("Segoe UI", 10))
        estilo.map("TButton", background=[("active", "black")], foreground=[("active", "white")])
        
        # Variable de control para la ventana de información completa
        self.ventana_info_abierta = None

        
        self.buscador_var = tk.StringVar()
        search_frame = tk.Frame(root, bg="#f0f0f0")
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(search_frame, text="Buscar:", bg="#f0f0f0").pack(side=tk.LEFT)
        search_entry = tk.Entry(search_frame, textvariable=self.buscador_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        search_entry.bind("<Return>", lambda e: self.buscar_contacto())
        tk.Button(search_frame, text="Buscar", command=self.buscar_contacto).pack(side=tk.RIGHT)

        list_frame = tk.Frame(root, bg="#f0f0f0")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        encabezados = tk.Frame(list_frame, bg="#f0f0f0")
        encabezados.pack(fill=tk.X)
        widths = [17, 12, 21, 12, 10, 20]  # Aquí agregamos el ancho para la dirección
        textos = ["Nombre Completo", "Teléfono", "Correo", "Ciudad", "Edad", "Dirección"]  # Añadimos "Dirección" en los encabezados
        for i, text in enumerate(textos):
            tk.Label(encabezados, text=text, width=widths[i], anchor="w", font=("Segoe UI", 10, "bold"), bg="#f0f0f0").pack(side=tk.LEFT)


        self.lista_contactos = tk.Listbox(list_frame, font=("Consolas", 10), height=20)
        self.lista_contactos.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(fill=tk.X)

        botones = [
            ("➕ Agregar", self.agregar_contacto),
            ("✏️ Editar", self.editar_contacto),
            ("🗑️ Eliminar", self.eliminar_contacto),
            ("💾 Exportar", self.exportar_contactos),
            ("📥 Importar", self.importar_contactos),
            ("📄 Ver Información Completa", self.ver_informacion_completa),
            ("❌ Salir", self.salir)
        ]

        columnas = 3
        filas = (len(botones) + columnas - 1) // columnas

        for i, (texto, accion) in enumerate(botones):
            row = i // columnas
            col = i % columnas
            boton = ttk.Button(btn_frame, text=texto, command=accion)
            boton.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

        for col in range(columnas):
            btn_frame.grid_columnconfigure(col, weight=1)

        self.ver_contactos()
        
    def ver_informacion_completa(self):
        seleccion = self.lista_contactos.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un contacto para ver la información completa.")
            return
        
        # Obtener el contacto seleccionado
        contacto = contactos[seleccion[0]]

        # Verificar si la ventana ya está abierta
        if not self.ventana_info_abierta or not self.ventana_info_abierta.winfo_exists():
            # Crear una nueva ventana para mostrar la información del contacto
            ventana_info = tk.Toplevel(self.root)
            ventana_info.title("Información Completa del Contacto")
            ventana_info.geometry("400x400")
            ventana_info.grab_set()

            # Al abrir la ventana de información completa, la marcamos como abierta
            self.ventana_info_abierta = ventana_info

            # Crear un frame para mostrar los datos del contacto
            frame_info = tk.Frame(ventana_info)
            frame_info.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # Datos del contacto a mostrar
            campos = [
                ("Nombre Completo", f"{contacto.get('nombre', '')} {contacto.get('apellido', '')}"),
                ("Teléfono", contacto.get('telefono', '')),
                ("Correo Electrónico", contacto.get('email', '')),
                ("Dirección", contacto.get('direccion', '')),
                ("Ciudad", contacto.get('ciudad', '')),
                ("Fecha de Nacimiento", contacto.get('fecha_nacimiento', '')),
            ]

            # Mostrar la información
            for i, (campo, valor) in enumerate(campos):
                label_dato = tk.Label(frame_info, text=f"{campo}:", font=("Segoe UI", 10, "bold"), anchor="w")
                label_dato.grid(row=i, column=0, padx=10, pady=5, sticky="w")
                
                label_valor = tk.Label(frame_info, text=valor, font=("Segoe UI", 10), anchor="w", width=25)
                label_valor.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            # Crear los botones de acción
            btn_frame = tk.Frame(ventana_info)
            btn_frame.pack(pady=10)

            # Función para editar el contacto
            def editar_contacto_completo():
                # Crear la ventana de edición, pero no cerrar la ventana de información completa
                self.ventana_contacto(nuevo=False, indice=seleccion[0])
                # Mantener la ventana de información completa en primer plano
                ventana_info.lift()  # Asegura que la ventana de información completa quede en primer plano.
                ventana_info.focus_force()  # Fuerza el foco en la ventana de información completa

            # Función para eliminar el contacto
            def eliminar_contacto_completo():
                respuesta = messagebox.askyesno("Eliminar", "¿Estás seguro de que deseas eliminar este contacto?")
                if respuesta:
                    self.eliminar_contacto()
                    ventana_info.destroy()  # Cerramos solo la ventana de información completa
                    self.ventana_info_abierta = None  # Actualizamos la variable para evitar errores

            # Crear los botones de acción
            btn_editar = tk.Button(btn_frame, text="Editar", width=10, command=editar_contacto_completo)
            btn_editar.pack(side=tk.LEFT, padx=10)

            btn_eliminar = tk.Button(btn_frame, text="Eliminar", width=10, command=eliminar_contacto_completo)
            btn_eliminar.pack(side=tk.LEFT, padx=10)

            # Botón para cerrar la ventana de información completa
            btn_cerrar = tk.Button(ventana_info, text="Cancelar", command=ventana_info.destroy)
            btn_cerrar.pack(pady=10)

            # Al cerrar la ventana de información completa, aseguramos que la variable se actualice
            ventana_info.protocol("WM_DELETE_WINDOW", lambda: self.ventana_info_abierta.destroy() or self.ventana_info_abierta.lift())
        
        else:
            # Si la ventana ya está abierta, simplemente le damos el foco
            self.ventana_info_abierta.lift()
            self.ventana_info_abierta.focus_force()



    def truncar_texto(self, texto, longitud):
        return texto if len(texto) <= longitud else texto[:longitud - 3] + "..."

    def formatear_fila(self, c, edad):
        nombre_completo = self.truncar_texto(f"{c.get('nombre', '')} {c.get('apellido', '')}", 15)  # Menos caracteres
        telefono = self.truncar_texto(c.get('telefono', ''), 12)  # Menos caracteres
        email = self.truncar_texto(c.get('email', ''), 20)  # Menos caracteres
        direccion = self.truncar_texto(c.get('direccion', ''), 15)  # Menos caracteres
        ciudad = self.truncar_texto(c.get('ciudad', ''), 10)  # Menos caracteres
        return f"{nombre_completo.ljust(18)} {telefono.ljust(14)} {email.ljust(22)} {direccion.ljust(17)} {ciudad.ljust(12)} {edad}"


    def buscar_contacto(self):
        texto = self.buscador_var.get().strip().lower()
        self.lista_contactos.delete(0, tk.END)
        for c in contactos:
            datos = " ".join(c.get(k, "") for k in c)
            if texto in datos.lower():
                edad = calcular_edad(c.get("fecha_nacimiento", ""))
                fila = self.formatear_fila(c, edad)
                self.lista_contactos.insert(tk.END, fila)

    def agregar_contacto(self):
        self.ventana_contacto(nuevo=True)

    def editar_contacto(self):
        seleccion = self.lista_contactos.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un contacto para editar.")
            return
        self.ventana_contacto(nuevo=False, indice=seleccion[0])

    def ventana_contacto(self, nuevo=True, indice=None):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Contacto" if nuevo else "Editar Contacto")
        ventana.geometry("400x470")
        ventana.grab_set()

        campos = [
            ("Nombre", "nombre"), ("Apellido", "apellido"), ("Teléfono", "telefono"),
            ("Correo electrónico", "email"), ("Dirección", "direccion"),
            ("Ciudad", "ciudad"), ("Fecha de nacimiento (YYYY-MM-DD)", "fecha_nacimiento")
        ]
        entradas = {}
        contacto_original = None

        if not nuevo:
            contacto_original = dict(contactos[indice])
            for texto, clave in campos:
                tk.Label(ventana, text=texto).pack()
                entrada = tk.Entry(ventana)
                entrada.insert(0, contacto_original.get(clave, ""))
                entrada.pack()
                entradas[clave] = entrada
        else:
            for texto, clave in campos:
                tk.Label(ventana, text=texto).pack()
                entrada = tk.Entry(ventana)
                entrada.pack()
                entradas[clave] = entrada

        def guardar_contacto():
            datos_actuales = {k: e.get().strip() for k, e in entradas.items()}

            # Verificar si ya existe el contacto (excluyendo el que se edita)
            if not nuevo:
                if contacto_existe(datos_actuales, indice_excluir=indice):
                    messagebox.showerror("Error", "Ya existe un contacto con la misma información (nombre, apellido o teléfono).")
                    return

                if contacto_original == datos_actuales:
                    messagebox.showwarning("Advertencia", "No has modificado nada del contacto.")
                    return

            # Si hay contacto con mismo nombre y apellido pero otro teléfono -> agregar sufijo al apellido
            apellido_base = datos_actuales["apellido"]
            sufijo = 1
            while any(
                i != indice and
                c["nombre"].lower() == datos_actuales["nombre"].lower() and
                c["apellido"].lower() == apellido_base.lower() and
                c["telefono"] != datos_actuales["telefono"]
                for i, c in enumerate(contactos)
            ):
                apellido_base = f"{datos_actuales['apellido']}{sufijo}"
                sufijo += 1

            if apellido_base != datos_actuales["apellido"]:
                entradas["apellido"].delete(0, tk.END)
                entradas["apellido"].insert(0, apellido_base)
                datos_actuales["apellido"] = apellido_base

            if nuevo:
                contactos.append(datos_actuales)
            else:
                contactos[indice] = datos_actuales

            guardar_contactos()
            self.ver_contactos()
            messagebox.showinfo("Éxito", "Contacto guardado correctamente.")
            ventana.destroy()

        def cancelar():
            ventana.destroy()

        btn_guardar = tk.Button(ventana, text="Guardar", width=15, command=guardar_contacto)
        btn_guardar.pack(pady=10)

        btn_cancelar = tk.Button(ventana, text="Cancelar", width=15, command=cancelar)
        btn_cancelar.pack(pady=10)

        ventana.bind('<Return>', lambda event: guardar_contacto())
        ventana.bind('<Escape>', lambda event: cancelar())





    # Función para buscar un contacto por nombre (para verificar duplicados por nombre)
    def buscar_contacto_por_nombre(nombre):
        for contacto in contactos:
            if contacto["nombre"].lower() == nombre.lower():
                return contacto
        return None

    def eliminar_contacto(self):
        seleccion = self.lista_contactos.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un contacto para eliminar.")
            return
        contacto = contactos[seleccion[0]]
        nombre = contacto.get('nombre', '') + " " + contacto.get('apellido', '')
        respuesta = messagebox.askyesno("Eliminar", f"¿Estás seguro de que deseas eliminar a {nombre}?")
        if respuesta:
            contactos.pop(seleccion[0])
            guardar_contactos()
            self.ver_contactos()

    def exportar_contactos(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json"), ("Texto", "*.txt")])
        if not ruta:
            return
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                if ruta.endswith(".json"):
                    json.dump(contactos, f, ensure_ascii=False, indent=4)
                elif ruta.endswith(".txt"):
                    for c in contactos:
                        f.write(f"{c['nombre']} {c['apellido']} | {c['telefono']} | {c['email']} | {c['direccion']} | {c['ciudad']} | {c['fecha_nacimiento']}\n")
            messagebox.showinfo("Éxito", "Contactos exportados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar los contactos: {str(e)}")

    def importar_contactos(self):
        ruta = filedialog.askopenfilename(
            filetypes=[
                ("Archivos de Contactos (.json, .txt)", "*.json *.txt"),
                ("Archivos JSON", "*.json"),
                ("Archivos de texto", "*.txt")
            ]
        )
        if not ruta:
            return

            try:
                if archivo.endswith(".json"):
                    with open(archivo, "r", encoding="utf-8") as f:
                        datos = json.load(f)
                else:  # Para archivos .txt
                    with open(archivo, "r", encoding="utf-8") as f:
                        datos = []
                        for linea in f:
                            partes = linea.strip().split(";")
                            if len(partes) == 3:
                                datos.append({
                                    "nombre": partes[0].strip(),
                                    "apellido": partes[1].strip(),
                                    "telefono": partes[2].strip()
                                })

                nuevos_contactos = 0
                for contacto in datos:
                    nombre = contacto["nombre"].strip().capitalize()
                    apellido_base = contacto["apellido"].strip().capitalize()
                    telefono = contacto["telefono"].strip()

                    if not nombre or not apellido_base or not telefono.isdigit():
                        continue  # Contacto inválido

                    # Buscar si el contacto ya existe exactamente
                    duplicado = any(
                        c["nombre"] == nombre and
                        c["apellido"] == apellido_base and
                        c["telefono"] == telefono
                        for c in contactos
                    )

                    if duplicado:
                        continue  # Contacto exactamente igual ya existe

                    # Verificar si existe contacto con mismo nombre completo pero otro teléfono
                    sufijo = 1
                    apellido_final = apellido_base
                    while any(
                        c["nombre"] == nombre and c["apellido"] == apellido_final
                        for c in contactos
                    ):
                        apellido_final = f"{apellido_base}{sufijo}"
                        sufijo += 1

                    contacto_nuevo = {
                        "nombre": nombre,
                        "apellido": apellido_final,
                        "telefono": telefono
                    }

                    contactos.append(contacto_nuevo)
                    nuevos_contactos += 1

                if nuevos_contactos > 0:
                    mostrar_contactos()
                    messagebox.showinfo("Importación exitosa", f"Se importaron {nuevos_contactos} contactos nuevos.")
                else:
                    messagebox.showinfo("Importación finalizada", "No se importaron nuevos contactos.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo importar el archivo:\n{str(e)}")



    def ver_contactos(self):
        self.lista_contactos.delete(0, tk.END)
        for c in contactos:
            # Calcular la edad del contacto
            edad = calcular_edad(c.get("fecha_nacimiento", ""))
            
            # Pasar la edad a la función formatear_fila
            fila = self.formatear_fila(c, edad)  # Ahora estamos pasando la edad
            
            self.lista_contactos.insert(tk.END, fila)



    def salir(self):
        self.root.quit()

# Configuración principal de la ventana
root = tk.Tk()
app = LibretaContactos(root)
cargar_contactos()  # Cargar los contactos al iniciar
root.mainloop()
