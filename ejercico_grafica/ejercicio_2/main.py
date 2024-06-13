import read
import charts


'''# Define a function to read data from a CSV file
def leer_datos(ruta_archivo):
    # Open the file in read mode
    with open(ruta_archivo, "r") as archivo_ventas:
        # Create a CSV reader object
        lector = csv.reader(archivo_ventas, delimiter=',')
        # Read the header row
        encabezados = next(lector)
        # Read the data rows and convert them to dictionaries
        datos = [dict(zip(encabezados, fila)) for fila in lector]
        # Return the data
        return datos
'''


# Define a function to run the program
def run():
    # Set the file path
    ruta_archivo = "ejercico_grafica\ejercicio_2\data_ventas.csv"
    try:
        # Read the data from the file
        data = read.leer(ruta_archivo)
    except FileNotFoundError:
        # Handle the error if the file is not found
        print("Error: El archivo CSV no existe")
        return

    # Ask the user to select a month
    meses_elegidos = input("Elegí el mes que quieres ver (separa por comas si son varios) o tipea 'todos': ")
    # Split the input into a list of months
    meses_elegidos = [x.strip().capitalize() for x in meses_elegidos.split(",")]

    # Check if the user wants to see all months
    if meses_elegidos == ['Todos']:
        # Extract the months and sales from the data
        labels = [x['Mes'] for x in data]
        values = [int(x['Ventas']) for x in data]
        # Generate a bar chart
        charts.generate_bar_chart(labels, values)
        # Generate a pie chart
        charts.generate_pie_chart(labels, values)
    else:
        # Filter the data by the selected months
        resultado = [x for x in data if x['Mes'] in meses_elegidos]
        if resultado:
            # Extract the months and sales from the filtered data
            labels = [x['Mes'] for x in resultado]
            values = [int(x['Ventas']) for x in resultado]
            # Generate a bar chart
            charts.generate_bar_chart(labels, values)
            # Generate a pie chart
            charts.generate_pie_chart(labels, values)
        else:
            # Handle the case where no data is found for the selected months
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
