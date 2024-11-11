#Programa: Imvestigación de la librería tkinter
#archivo: LAB6_EJER11.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 04/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Ejecutar el formulario 
import os
import tkinter as tk
from PIL import Image, ImageTk


main = tk.Tk()
main.resizable(False, False)


ROOT_DIR = os.path.abspath(os.curdir)
origin = Image.open(os.path.join(ROOT_DIR, "img", "grupo.png"))
resized = origin.resize((800, 600))

image = ImageTk.PhotoImage(resized)

canvas = tk.Canvas(main, width=image.width(), height=image.height())
canvas.pack()

canvas.create_image(image.width()//2, image.height()//2, anchor="center", image=image)
canvas.create_text(image.width()//2, 30, text="Grupo 1: Los Divinos", fill="white", font=("consolas", 40))
canvas.create_text(image.width()//2, 90, text="1. Elmer Montoya (Elmer Galarga) ", fill="white", font=("consolas", 20))
canvas.create_text(image.width()//2, 120, text="2. Elvis Aguilar (Elvis Amoroso)", fill="white", font=("consolas", 20))
canvas.create_text(image.width()//2, 150, text="3. Joseph Avilez (Joseph Smith)", fill="white", font=("consolas", 20))
canvas.create_text(image.width()//2, 180, text="4. Rafael Argüello (???)", fill="white", font=("consolas", 20))
main.mainloop()