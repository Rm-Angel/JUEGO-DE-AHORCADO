import tkinter as tk
import random

palabras = ["python", "ahorcado", "programacion", "inteligencia", "asistente"]

class AhorcadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Juego del Ahorcado")
        self.palabra_secreta = random.choice(palabras)
        self.letras_adivinadas = []
        self.intentos = 0
        self.intentos_maximos = 6

        # Canvas para dibujar el ahorcado
        self.canvas = tk.Canvas(root, width=200, height=250, bg="white")
        self.canvas.pack(pady=10)
        self.dibujar_base()

        # Elementos de texto
        self.label_palabra = tk.Label(root, text="", font=("Arial", 24))
        self.label_palabra.pack()

        self.entry_letra = tk.Entry(root, font=("Arial", 14), width=5)
        self.entry_letra.pack()

        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.adivinar)
        self.boton_adivinar.pack(pady=5)

        self.label_mensaje = tk.Label(root, text="", font=("Arial", 14))
        self.label_mensaje.pack()

        self.label_intentos = tk.Label(root, text="Intentos: 0 / 6", font=("Arial", 12))
        self.label_intentos.pack()

        self.boton_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack(pady=10)

        self.actualizar_palabra()

    def dibujar_base(self):
        # Estructura del ahorcado
        self.canvas.create_line(20, 230, 180, 230)  # base
        self.canvas.create_line(50, 230, 50, 20)    # poste vertical
        self.canvas.create_line(50, 20, 130, 20)    # poste horizontal
        self.canvas.create_line(130, 20, 130, 40)   # cuerda

    def dibujar_ahorcado(self):
        partes = [
            lambda: self.canvas.create_oval(110, 40, 150, 80),         # cabeza
            lambda: self.canvas.create_line(130, 80, 130, 140),        # cuerpo
            lambda: self.canvas.create_line(130, 90, 100, 110),        # brazo izquierdo
            lambda: self.canvas.create_line(130, 90, 160, 110),        # brazo derecho
            lambda: self.canvas.create_line(130, 140, 110, 180),       # pierna izquierda
            lambda: self.canvas.create_line(130, 140, 150, 180),       # pierna derecha
        ]
        if self.intentos <= len(partes):
            partes[self.intentos - 1]()  # dibuja la parte correspondiente

    def actualizar_palabra(self):
        estado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                estado += letra + " "
            else:
                estado += "_ "
        self.label_palabra.config(text=estado.strip())

    def adivinar(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if not letra or len(letra) != 1 or not letra.isalpha():
            self.label_mensaje.config(text="❗ Ingresa una letra válida.")
            return

        if letra in self.letras_adivinadas:
            self.label_mensaje.config(text="⚠️ Ya usaste esa letra.")
            return

        self.letras_adivinadas.append(letra)

        if letra in self.palabra_secreta:
            self.label_mensaje.config(text="✅ ¡Bien! La letra está.")
        else:
            self.intentos += 1
            self.label_mensaje.config(text="❌ La letra no está.")
            self.dibujar_ahorcado()

        self.label_intentos.config(text=f"Intentos: {self.intentos} / {self.intentos_maximos}")
        self.actualizar_palabra()

        if all(letra in self.letras_adivinadas for letra in self.palabra_secreta):
            self.label_mensaje.config(text=f"🎉 ¡Ganaste! Era: {self.palabra_secreta}")
            self.boton_adivinar.config(state="disabled")
        elif self.intentos >= self.intentos_maximos:
            self.label_mensaje.config(text=f"💀 Perdiste. Era: {self.palabra_secreta}")
            self.boton_adivinar.config(state="disabled")

    def reiniciar(self):
        self.palabra_secreta = random.choice(palabras)
        self.letras_adivinadas = []
        self.intentos = 0
        self.label_mensaje.config(text="")
        self.label_intentos.config(text="Intentos: 0 / 6")
        self.boton_adivinar.config(state="normal")
        self.canvas.delete("all")
        self.dibujar_base()
        self.actualizar_palabra()

# Ejecutar la app
root = tk.Tk()
app = AhorcadoApp(root)
root.mainloop()