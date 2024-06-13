import csv
import main


        

def leer(ruta_archivo):
    with open(ruta_archivo, "r") as archivo_ventas:
        lector = csv.reader(archivo_ventas, delimiter=',')
        archivo_ventas.seek(0)
        encabezados = next(lector)
        datos = [dict(zip(encabezados, fila)) for fila in lector]
        return datos

# Función para escribir datos en un archivo CSV
def escribir_datos(ruta_archivo, datos):
    # Abrir el archivo en modo binario de lectura y escritura
    with open(ruta_archivo, "ab+") as archivo_ventas:
        # Mover el puntero del archivo al principio del archivo
        archivo_ventas.seek(0)
        # Crear un objeto escritor CSV con delimitador de coma
        escritor = csv.writer(archivo_ventas, delimiter=',')
        # Escribir los datos en el archivo CSV
        escritor.writerows(datos)
        # Devolver True para indicar éxito
        return True

# Función para agregar una nueva fila a un archivo CSV
def agregar_fila(ruta_archivo, datos):
    # Abrir el archivo en modo binario de lectura y escritura
    with open(ruta_archivo, "ab+") as archivo_ventas:
        # Mover el puntero del archivo al principio del archivo
        archivo_ventas.seek(0)
        # Crear un objeto escritor CSV con delimitador de coma
        escritor = csv.writer(archivo_ventas, delimiter=',')
        # Escribir la nueva fila en el archivo CSV
        escritor.writerow(datos)
        # Devolver True para indicar éxito
        return True

# Función para eliminar una fila de un archivo CSV según un ID
def eliminar_fila(ruta_archivo, id):
    # Leer los datos del archivo CSV
    datos = leer(ruta_archivo)
    # Iterar sobre cada fila en los datos
    for i in range(len(datos)):
        # Verificar si el ID en la fila actual coincide con el ID dado
        if datos[i][0] == id:
            # Eliminar la fila de la lista de datos
            del datos[i]
            # Salir del bucle
            break
    # Escribir los datos actualizados de vuelta en el archivo CSV
    escribir_datos(ruta_archivo, datos)
    # Devolver True para indicar éxito
    return True

# Función para buscar una fila en un archivo CSV según un ID
def buscar_fila(ruta_archivo, id):
    datos = leer(ruta_archivo)
    for fila in datos:
      if fila[0] == id:
       return fila

if __name__ == '__main__':
    main.run()
