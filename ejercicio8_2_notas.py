import math
import tkinter as tk
from tkinter import messagebox


class Notas:

    def __init__(self):
        self.lista_notas = [0, 0, 0, 0, 0]

    def calcular_promedio(self):
        suma = 0
        for nota in self.lista_notas:
            suma = suma + nota
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = 0
        for nota in self.lista_notas:
            suma = suma + math.pow(nota - promedio, 2)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota > mayor:
                mayor = nota
        return mayor

    def calcular_menor(self):
        menor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota < menor:
                menor = nota
        return menor


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.resizable(False, False)
        self.inicio()
        x = (self.winfo_screenwidth() - 280) // 2
        y = (self.winfo_screenheight() - 380) // 2
        self.geometry("280x380+" + str(x) + "+" + str(y))

    def inicio(self):
        self.campos = []
        for i in range(5):
            etiqueta = tk.Label(self, text="Nota " + str(i + 1) + ":", anchor="w")
            etiqueta.place(x=20, y=20 + 30 * i, width=80, height=23)
            campo = tk.Entry(self)
            campo.place(x=105, y=20 + 30 * i, width=135, height=23)
            self.campos.append(campo)

        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=20, y=170, width=100, height=26)

        self.boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=125, y=170, width=80, height=26)

        self.etiqueta_promedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.etiqueta_promedio.place(x=20, y=215, width=240, height=23)

        self.etiqueta_desviacion = tk.Label(self, text="Desviación estándar = ", anchor="w")
        self.etiqueta_desviacion.place(x=20, y=245, width=240, height=23)

        self.etiqueta_mayor = tk.Label(self, text="Nota mayor = ", anchor="w")
        self.etiqueta_mayor.place(x=20, y=275, width=240, height=23)

        self.etiqueta_menor = tk.Label(self, text="Nota menor = ", anchor="w")
        self.etiqueta_menor.place(x=20, y=305, width=240, height=23)

    def calcular(self):
        notas = Notas()
        for i in range(5):
            texto = self.campos[i].get().strip()
            if texto == "":
                messagebox.showwarning("Falta una nota",
                                       "Debe ingresar las cinco notas, falta la nota " + str(i + 1) + ".")
                return
            try:
                notas.lista_notas[i] = float(texto.replace(",", "."))
            except ValueError:
                messagebox.showwarning("Dato no válido",
                                       "La nota " + str(i + 1) + " debe ser un número.")
                return

        self.etiqueta_promedio.config(text=f"Promedio = {notas.calcular_promedio():.2f}")
        self.etiqueta_desviacion.config(text=f"Desviación estándar = {notas.calcular_desviacion():.2f}")
        self.etiqueta_mayor.config(text=f"Nota mayor = {notas.calcular_mayor():.2f}")
        self.etiqueta_menor.config(text=f"Nota menor = {notas.calcular_menor():.2f}")

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.etiqueta_promedio.config(text="Promedio = ")
        self.etiqueta_desviacion.config(text="Desviación estándar = ")
        self.etiqueta_mayor.config(text="Nota mayor = ")
        self.etiqueta_menor.config(text="Nota menor = ")


ventana = VentanaPrincipal()
ventana.mainloop()
