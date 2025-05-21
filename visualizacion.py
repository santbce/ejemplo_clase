# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# seaborn para visualizacion mas estilizadas 
import seaborn as sns
import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox



from Analisis import DataAnalyzer

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)

info = analizar.summary()

def informacion():
        
        text_area.delete("1.0", tk.END) #Para vaciar al ejecutar 
        info = analizar.summary()
        text_area.insert(tk.END, info)
        try:
                text_area.delete("1.0", tk.END) #Para vaciar al ejecutar
                info = analizar.summary()
                text_area.insert(tk.END, info)
        except:
                messagebox.showerror("Error", "No se puede obtener la informacion de DataFrame")        

def mostrar_imagenes (pil_img):
        image_tk = ImageTk.PhotoImage(pil_img)
        image_label.config(image=image_tk)
        image_label.image = image_tk     

def mostrar_correlacion():
        img= analizar.correlation_matrix()
        mostrar_imagenes(img)  

def mostrar_categorico():
        cols = analizar.df.select_dtypes(include = "object").columns.tolist()
        if not cols:
                messagebox.showwarning("Atencion", "El df no tiene col. categoricas")
        else:
                sel= simpledialog.askstring("Columna", f"Elige una: \n {cols}")
                if sel in cols:
                        img= analizar.categorical_analisis_col(sel)
                        mostrar_imagenes(img)    


def agregar_muestra():
    columnas = analizar.df.columns.tolist()
    nueva_muestra = {}
    
    for col in columnas:
        valor = simpledialog.askstring("Entrada de datos", f"Ingrese el valor para '{col}':")
        if valor is None: 
            return
        nueva_muestra[col] = valor

    nueva_fila_df = pd.DataFrame([nueva_muestra])
    analizar.df = pd.concat([analizar.df, nueva_fila_df], ignore_index=True)
    analizar.df.to_csv("adult.csv", index=False)
    
    messagebox.showinfo("Éxito", "Nueva muestra añadida y guardada correctamente.")

                         
  


ventana = tk.Tk()
ventana.title("Analizis de datos")
boton_summary = tk.Button(ventana, text= "info", command= informacion)
boton_summary.pack()

text_area = tk.scrolledtext.ScrolledText(ventana, width = 70, height = 30, )
text_area.pack()
ventana.mainloop()

boton_numerico = tk.Button(ventana, text= "Numerico", command= mostrar_correlacion )
boton_numerico.grid(row = 0, column=1,padx=10, pady=10 )

boton_categorico = tk.Button(ventana, text= "Categorico", command= mostrar_categorico)
boton_categorico.grid(row = 0, column=2, padx=10, pady=10)

text_area = ScrolledText(ventana, width= 70, height=30)
text_area.grid(row= 1, column= 2)

boton_muestra = tk.Button(ventana, text="Agregar muestra", command=agregar_muestra)
boton_muestra.grid(row=0, column=3, padx=10, pady=10)


content_frame= tk.Frame(ventana)
content_frame.grid(row = 1, column=2, padx=10, pady=10)
image_label = tk.Label(content_frame)
image_label.grid(row = 0, column=0, padx=10, pady=10)
ventana.mainloop()

