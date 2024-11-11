#Programa: Imvestigación de la librería tkinter
#archivo: LAB6_EJER10.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 04/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Ejecutar el formulario con dos imágenes
import os
import tkinter as tk
from tkinter import PhotoImage


main = tk.Tk()
main.title("TK Frames")

frame = tk.Frame(main)
frame.pack()

ROOT_DIR = os.path.abspath(os.curdir)
image1 = PhotoImage(file=os.path.join(ROOT_DIR, "img", "scenery_small.png"))
image2 = PhotoImage(file=os.path.join(ROOT_DIR, "img", "scenery_small_grey.png"))

label1 = tk.Label(frame, image=image1)
label1.pack(side="left")
label2 = tk.Label(frame, image=image2)
label2.pack(side="right")

main.mainloop()