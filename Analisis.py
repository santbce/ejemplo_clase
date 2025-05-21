# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# seaborn para visualizacion mas estilizadas 
import seaborn as sns
import os
import io

class DataAnalyzer:
    def __init__(self, data):
      self.df = data

    def summary(self):
      buffer = io.StringIO()
      self.df.info(buf = buffer)
      salida = buffer.getvalue()
      salida_describe = self.df.describe().to_string()
      salida += "\n\n" + salida_describe
      return salida 

    def missing_values(self):
      return self.df.isnull()

    def imprimir(self):
      print("hola")

    def correlation_matrix(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        corr_matrix = self.df[numeric_cols].corr()
        plt.figure()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Matriz de Correlación')
        plt.show() 

    def categorical_analisis(self):
       categorical_cols = self.df.select_dtypes(include = 'object').columns
       print(f"Las columnas categoricas son {categorical_cols}")
       column = input("Digiete la columna a visualizar:") 
       
       
       
       if column in categorical_cols:
        plt.figure()
        sns.countplot(data = self.df, x= column, order= self.df[column].value_counts().index)
        plt.xticks(rotation = 45)
        plt.show()
       else:
        print("La colunma no es categorica o esta mal escrita")
                
