import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:

    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        self.volumen = volumen

    def get_superficie(self):
        return self.superficie

    def set_superficie(self, superficie):
        self.superficie = superficie


class Cilindro(FiguraGeometrica):

    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        self.set_volumen(math.pi * self.altura * math.pow(self.radio, 2))
        return self.get_volumen()

    def calcular_superficie(self):
        lado_a = 2 * math.pi * self.radio * self.altura
        lado_b = 2 * math.pi * math.pow(self.radio, 2)
        self.set_superficie(lado_a + lado_b)
        return self.get_superficie()


class Esfera(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        self.set_volumen(4 / 3 * math.pi * math.pow(self.radio, 3))
        return self.get_volumen()

    def calcular_superficie(self):
        self.set_superficie(4 * math.pi * math.pow(self.radio, 2))
        return self.get_superficie()


class Piramide(FiguraGeometrica):

    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        self.set_volumen(math.pow(self.base, 2) * self.altura / 3)
        return self.get_volumen()

    def calcular_superficie(self):
        area_base = math.pow(self.base, 2)
        area_lados = 2 * self.base * self.apotema
        self.set_superficie(area_base + area_lados)
        return self.get_superficie()


class Cubo(FiguraGeometrica):

    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_volumen(self):
        self.set_volumen(math.pow(self.lado, 3))
        return self.get_volumen()

    def calcular_superficie(self):
        self.set_superficie(6 * math.pow(self.lado, 2))
        return self.get_superficie()


class Prisma(FiguraGeometrica):

    def __init__(self, base, ancho, altura):
        super().__init__()
        self.base = base
        self.ancho = ancho
        self.altura = altura

    def calcular_volumen(self):
        self.set_volumen(self.base * self.ancho * self.altura)
        return self.get_volumen()

    def calcular_superficie(self):
        area = 2 * (self.base * self.ancho + self.base * self.altura + self.ancho * self.altura)
        self.set_superficie(area)
        return self.get_superficie()


class VentanaFigura(tk.Toplevel):

    def __init__(self, padre, titulo, campos, clase_figura):
        super().__init__(padre)
        self.title(titulo)
        self.resizable(False, False)
        self.clase_figura = clase_figura
        self.inicio(campos)

    def inicio(self, nombres_campos):
        self.campos = []
        y = 20
        for nombre in nombres_campos:
            etiqueta = tk.Label(self, text=nombre, anchor="w")
            etiqueta.place(x=20, y=y, width=100, height=23)
            campo = tk.Entry(self)
            campo.place(x=125, y=y, width=135, height=23)
            self.campos.append(campo)
            y = y + 30

        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=125, y=y, width=135, height=26)

        self.etiqueta_volumen = tk.Label(self, text="Volumen = ", anchor="w")
        self.etiqueta_volumen.place(x=20, y=y + 40, width=260, height=23)

        self.etiqueta_superficie = tk.Label(self, text="Superficie = ", anchor="w")
        self.etiqueta_superficie.place(x=20, y=y + 70, width=260, height=23)

        # imagen de la figura (parte propuesta)
        self.lienzo = tk.Canvas(self, width=140, height=140, bg="white",
                                highlightthickness=1, highlightbackground="gray")
        self.lienzo.place(x=300, y=20)
        self.dibujar(self.lienzo)

        alto = max(y + 110, 190)
        self.geometry("460x" + str(alto))

    def dibujar(self, lienzo):
        pass

    def calcular(self):
        valores = []
        for campo in self.campos:
            texto = campo.get().strip().replace(",", ".")
            try:
                valores.append(float(texto))
            except ValueError:
                messagebox.showwarning("Dato no válido", "Todos los campos deben ser números.")
                return

        figura = self.clase_figura(*valores)
        volumen = figura.calcular_volumen()
        superficie = figura.calcular_superficie()
        self.etiqueta_volumen.config(text=f"Volumen = {volumen:.2f} cm³")
        self.etiqueta_superficie.config(text=f"Superficie = {superficie:.2f} cm²")


class VentanaCilindro(VentanaFigura):

    def __init__(self, padre):
        super().__init__(padre, "Cilindro", ["Radio (cm):", "Altura (cm):"], Cilindro)

    def dibujar(self, lienzo):
        lienzo.create_oval(30, 100, 110, 124, fill="#cfe2f3", outline="black")
        lienzo.create_rectangle(31, 32, 110, 112, fill="#cfe2f3", outline="")
        lienzo.create_line(30, 32, 30, 112)
        lienzo.create_line(110, 32, 110, 112)
        lienzo.create_oval(30, 20, 110, 44, fill="#e8f1fa", outline="black")


class VentanaEsfera(VentanaFigura):

    def __init__(self, padre):
        super().__init__(padre, "Esfera", ["Radio (cm):"], Esfera)

    def dibujar(self, lienzo):
        lienzo.create_oval(20, 20, 120, 120, fill="#d9ead3", outline="black")
        lienzo.create_oval(20, 60, 120, 80, outline="gray", dash=(3, 3))


class VentanaPiramide(VentanaFigura):

    def __init__(self, padre):
        super().__init__(padre, "Pirámide", ["Base (cm):", "Altura (cm):", "Apotema (cm):"], Piramide)

    def dibujar(self, lienzo):
        lienzo.create_line(25, 105, 50, 75, dash=(3, 3))
        lienzo.create_line(50, 75, 125, 95, dash=(3, 3))
        lienzo.create_line(70, 15, 50, 75, dash=(3, 3))
        lienzo.create_polygon(70, 15, 25, 105, 100, 125, fill="#fce5cd", outline="black")
        lienzo.create_polygon(70, 15, 100, 125, 125, 95, fill="#f9cb9c", outline="black")


class VentanaCubo(VentanaFigura):

    def __init__(self, padre):
        super().__init__(padre, "Cubo", ["Lado (cm):"], Cubo)

    def dibujar(self, lienzo):
        lienzo.create_polygon(30, 50, 90, 50, 90, 110, 30, 110, fill="#d9d2e9", outline="black")
        lienzo.create_polygon(30, 50, 55, 25, 115, 25, 90, 50, fill="#ece8f5", outline="black")
        lienzo.create_polygon(90, 50, 115, 25, 115, 85, 90, 110, fill="#b4a7d6", outline="black")


class VentanaPrisma(VentanaFigura):

    def __init__(self, padre):
        super().__init__(padre, "Prisma", ["Base (cm):", "Ancho (cm):", "Altura (cm):"], Prisma)

    def dibujar(self, lienzo):
        lienzo.create_polygon(15, 60, 100, 60, 100, 110, 15, 110, fill="#fff2cc", outline="black")
        lienzo.create_polygon(15, 60, 40, 35, 125, 35, 100, 60, fill="#fff9e6", outline="black")
        lienzo.create_polygon(100, 60, 125, 35, 125, 85, 100, 110, fill="#ffe599", outline="black")


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.resizable(False, False)
        self.inicio()
        x = (self.winfo_screenwidth() - 460) // 2
        y = (self.winfo_screenheight() - 170) // 2
        self.geometry("460x170+" + str(x) + "+" + str(y))

    def inicio(self):
        titulo = tk.Label(self, text="Seleccione la figura geométrica")
        titulo.place(x=20, y=20, width=420, height=23)

        self.boton_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        self.boton_cilindro.place(x=20, y=70, width=78, height=28)

        self.boton_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        self.boton_esfera.place(x=104, y=70, width=78, height=28)

        self.boton_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        self.boton_piramide.place(x=188, y=70, width=78, height=28)

        self.boton_cubo = tk.Button(self, text="Cubo", command=self.abrir_cubo)
        self.boton_cubo.place(x=272, y=70, width=78, height=28)

        self.boton_prisma = tk.Button(self, text="Prisma", command=self.abrir_prisma)
        self.boton_prisma.place(x=356, y=70, width=78, height=28)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

    def abrir_cubo(self):
        VentanaCubo(self)

    def abrir_prisma(self):
        VentanaPrisma(self)


ventana = VentanaPrincipal()
ventana.mainloop()
