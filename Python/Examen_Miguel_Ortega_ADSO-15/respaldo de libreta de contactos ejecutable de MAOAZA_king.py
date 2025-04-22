######################################### Mini Sistema: Agenda de Contactos de 👑 👑 MAOAZA_king ☯ ☯########################################
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import os
import json
from datetime import datetime

contactos = []


def guardar_contactos():
    with open("contactos.json", "w", encoding="utf-8") as f:
        json.dump(contactos, f, ensure_ascii=False, indent=4)


def cargar_contactos():
    global contactos
    if os.path.exists("contactos.json"):
        with open("contactos.json", "r", encoding="utf-8") as f:
            contactos = json.load(f)


def calcular_edad(fecha_nacimiento):
    try:
        fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.today()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return str(edad)
    except:
        return "N/A"


def validar_fecha(fecha):
    try:
        f = datetime.strptime(fecha, "%Y-%m-%d")
        return f <= datetime.today()
    except:
        return False


def validar_datos_contacto(datos):
    if not any(c.isalpha() for c in datos["nombre"]):
        return "El nombre debe contener al menos una letra."
    if not any(c.isalpha() for c in datos["apellido"]):
        return "El apellido debe contener al menos una letra."
    if not datos["telefono"].isdigit():
        return "El teléfono debe contener solo números."
    if "@" not in datos["email"] or "." not in datos["email"]:
        return "El correo debe contener '@' y '.'."
    if any(c.isdigit() for c in datos["ciudad"]):
        return "La ciudad no debe contener números."
    if not validar_fecha(datos["fecha_nacimiento"]):
        return "La fecha de nacimiento no puede ser futura o inválida."
    return None


class LibretaContactos:
    def __init__(self, root):
        self.root = root
        self.root.title("📘 Libreta de Contactos")
        self.root.geometry("800x550")
        self.root.minsize(800, 550)
        self.root.configure(bg="#f0f0f0")

        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("TButton", padding=6, background="#5bbcfc", foreground="black", font=("Segoe UI", 10))
        estilo.map("TButton", background=[("active", "black")], foreground=[("active", "white")])

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
        widths = [17, 12, 21, 12, 10]
        textos = ["Nombre Completo", "Teléfono", "Correo", "Ciudad", "Edad"]
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
            ("📄 Ver Todos", self.ver_contactos),
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

    def truncar_texto(self, texto, longitud):
        return texto if len(texto) <= longitud else texto[:longitud - 3] + "..."

    def formatear_fila(self, c, edad):
        nombre_completo = self.truncar_texto(f"{c.get('nombre', '')} {c.get('apellido', '')}", 20)
        telefono = self.truncar_texto(c.get('telefono', ''), 15)
        email = self.truncar_texto(c.get('email', ''), 25)
        ciudad = self.truncar_texto(c.get('ciudad', ''), 15)
        return f"{nombre_completo.ljust(20)}{telefono.ljust(15)}{email.ljust(25)}{ciudad.ljust(15)}{edad}"

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
        for texto, clave in campos:
            tk.Label(ventana, text=texto).pack()
            entrada = tk.Entry(ventana)
            if not nuevo:
                entrada.insert(0, contactos[indice].get(clave, ""))
            entrada.pack()
            entradas[clave] = entrada

        def guardar():
            datos = {k: e.get().strip() for k, e in entradas.items()}
            error = validar_datos_contacto(datos)
            if error:
                messagebox.showerror("Error", error)
                return
            if nuevo:
                contactos.append(datos)
            else:
                contactos[indice] = datos
            guardar_contactos()
            self.ver_contactos()
            ventana.destroy()

        ventana.bind("<Return>", lambda e: guardar())

        btn_frame = tk.Frame(ventana)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Guardar", width=10, command=guardar).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", width=10, command=ventana.destroy).pack(side=tk.RIGHT, padx=10)

    def eliminar_contacto(self):
        seleccion = self.lista_contactos.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un contacto para eliminar.")
            return
        contacto = contactos[seleccion[0]]
        nombre = contacto.get('nombre', '') + " " + contacto.get('apellido', '')
        confirmar = messagebox.askyesno("Confirmar Eliminación", f"¿Deseas eliminar a:\n\n{nombre}?")
        if confirmar:
            contactos.pop(seleccion[0])
            guardar_contactos()
            self.ver_contactos()
            messagebox.showinfo("Eliminado", f"Contacto '{nombre}' eliminado.")

    def exportar_contactos(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".txt")
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                for c in contactos:
                    fila = ",".join([c.get("nombre", ""), c.get("apellido", ""), c.get("telefono", ""),
                                     c.get("email", ""), c.get("direccion", ""), c.get("ciudad", ""), c.get("fecha_nacimiento", "")])
                    f.write(fila + "\n")
            messagebox.showinfo("Éxito", "Contactos exportados correctamente.")

    def importar_contactos(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivo de texto", "*.txt")], title="Seleccionar archivo a importar")
        if not ruta:
            return
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                lineas = f.readlines()
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 7:
                    continue
                nombre, apellido, telefono, email, direccion, ciudad, fecha_nacimiento = partes
                nuevo = {
                    "nombre": nombre, "apellido": apellido, "telefono": telefono,
                    "email": email, "direccion": direccion, "ciudad": ciudad, "fecha_nacimiento": fecha_nacimiento
                }
                if any(all(nuevo[k] == c.get(k, "") for k in nuevo) for c in contactos):
                    continue
                apellidos_existentes = {c["apellido"] for c in contactos if c["nombre"] == nombre}
                base = apellido
                i = 1
                while nuevo["apellido"] in apellidos_existentes:
                    nuevo["apellido"] = f"{base}{i}"
                    i += 1
                contactos.append(nuevo)
            guardar_contactos()
            self.ver_contactos()
            messagebox.showinfo("Importado", "Contactos importados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ver_contactos(self):
        self.lista_contactos.delete(0, tk.END)
        for c in contactos:
            edad = calcular_edad(c.get("fecha_nacimiento", ""))
            fila = self.formatear_fila(c, edad)
            self.lista_contactos.insert(tk.END, fila)

    def salir(self):
        guardar_contactos()
        self.root.quit()


if __name__ == '__main__':
    cargar_contactos()
    root = tk.Tk()
    app = LibretaContactos(root)
    root.mainloop()