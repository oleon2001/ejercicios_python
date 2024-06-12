

import read
import charts



'''
def leer_datos(ruta_archivo):
    with open(ruta_archivo, "r") as archivo_ventas:
        lector = csv.reader(archivo_ventas, delimiter=',')
        encabezados = next(lector)
        datos = [dict(zip(encabezados, fila)) for fila in lector]
        return datos
'''

def run():
    ruta_archivo = "/home/oleon/Escritorio/ejercicios_python/ejercico_grafica/ejercicio_2/data_ventas.csv"
    data = read.leer(ruta_archivo)
    meses_elegidos = input("Elegí el mes que quieres ver (separa por comas si son varios) o tipea 'todos': ")
    meses_elegidos = [x.strip() for x in meses_elegidos.split(",")]
    if str(meses_elegidos).capitalize() == 'Todos':
        labels = [x['Mes'] for x in data]
        values = [int(x['Ventas']) for x in data]
        charts.generate_bar_chart(labels, values)
        charts.generate_pie_chart(labels, values)
    elif str(meses_elegidos).capitalize() == 'Todos':
        resultado = [x for x in data if x['Mes'] == meses_elegidos]
        labels = [x['Mes'] for x in resultado]
        values = [int(x['Ventas']) for x in resultado]
        charts.generate_bar_chart(labels, values)
        charts.generate_pie_chart(labels, values)
    else:
        print("No se encontraron datos para el mes seleccionado")

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