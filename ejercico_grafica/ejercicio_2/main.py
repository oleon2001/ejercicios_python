
import csv
import charts
import read

'''
def leer_datos(ruta_archivo):
    with open(ruta_archivo, "r") as archivo_ventas:
        lector = csv.reader(archivo_ventas, delimiter=',')
        encabezados = next(lector)
        datos = [dict(zip(encabezados, fila)) for fila in lector]
        return datos
'''

def run():
    ruta_archivo = "ejercicio_2/data_ventas.csv"
    data = read.leer(ruta_archivo)
    mes_elegido = input("Elegí el mes que quieres ver o tipea 'todos': ")
    if mes_elegido == 'todos':
        labels = [x['Mes'] for x in data]
        values = [int(x['Ventas']) for x in data]
        charts.generate_bar_chart(labels, values)
        charts.generate_pie_chart(labels, values)
    else:
        resultado = [x for x in data if x['Mes'] == mes_elegido]
        labels = [x['Mes'] for x in resultado]
        values = [int(x['Ventas']) for x in resultado]
        charts.generate_bar_chart(labels, values)
        charts.generate_pie_chart(labels, values)
    

if __name__ == '__main__':
    run()

'''
    if mes_elegido == 'todos':
        for fila in data:
            print(fila)
    elif mes_elegido in primera_columna:
        for fila in data:
            if fila[0] == mes_elegido:
                print(fila)
    else:
        print("No existe ese mes")
'''
if __name__ == '__main__':
    run()