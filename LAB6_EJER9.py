#Programa: Imvestigación de la librería tkinter
#archivo: LAB6_EJER9.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 04/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Ejecutar el formulario 
import os
import tkinter as tk


main = tk.Tk()


ROOT_DIR = os.path.abspath(os.curdir)
image = tk.PhotoImage(file=os.path.join(ROOT_DIR, "img", "scenery_small.png"))

canvas = tk.Canvas(main, width=image.width(), height=image.height())
canvas.pack()

canvas.create_image(image.width()//2, image.height()//2, anchor="center", image=image)
canvas.create_text(image.width()//2, 20, text="Hola TKinter", fill="white")
main.mainloop()