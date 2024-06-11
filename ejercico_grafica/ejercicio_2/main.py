import csv

def leer_ruta(ruta_archivo):
    with open(ruta_archivo, "r") as archivo_ventas:
        lector = csv.reader(archivo_ventas, delimiter=',')
        datos = [fila for fila in lector]
        return datos

def run():
    ruta_archivo = 'ejercicio_2/data_ventas.csv'
    datos = leer_ruta(ruta_archivo)
    primera_columna = [fila[0] for fila in datos]
    
    str(mes_elegido).capitalize() = input("Elegi el mes que quieres ver o tipea 'todos': ")
    
    if mes_elegido == 'todos':
        for fila in datos:
            print(fila)
    else:
        mostrar_data = [fila for fila in datos if fila[0] == mes_elegido]
        if mostrar_data:
            for fila in mostrar_data:
                print(fila)
        else:
            print("No existe ese mes")

if __name__ == '__main__':
    run()