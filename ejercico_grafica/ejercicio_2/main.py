import read
import utils
import csv

def run():
    mes_elegido=input("elegi el mes que quieres ver o tipea todos:")
    data=read.leer_ruta('ejercicio_2/data_ventas.csv')
    primera_columna = [fila[0] for fila in data]
    if mes_elegido == str(primera_columna):
     mostrar_data=list(map(lambda x: x['Mes']==mes_elegido,data))
     print(mostrar_data)
    elif mes_elegido == 'todos':
      for fila in data:
         print(fila)
    else:
      print("no existe ese mes")

    





if __name__ == '__main__':
   run()