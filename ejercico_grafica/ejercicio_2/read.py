import csv

# Function to read data from a CSV file
def leer(path):
    # Open the file in binary read and write mode
    with open(path, "ab+") as archivo_ventas:
        # Move the file pointer to the beginning of the file
        archivo_ventas.seek(0)
        # Create a CSV reader object with a comma delimiter
        reader = csv.reader(archivo_ventas, delimiter=',')
        # Initialize an empty list to store the data
        data = []
        # Iterate over each row in the CSV file
        for row in reader:
            # Append the row to the data list
            data.append(row)
        # Return the data list
        return data

# Function to write data to a CSV file
def escribir(path, data):
    # Open the file in binary read and write mode
    with open(path, "ab+") as archivo_ventas:
        # Move the file pointer to the beginning of the file
        archivo_ventas.seek(0)
        # Create a CSV writer object with a comma delimiter
        writer = csv.writer(archivo_ventas, delimiter=',')
        # Write the data to the CSV file
        writer.writerows(data)
        # Return True to indicate success
        return True

# Function to add a new row to a CSV file
def agregar(path, data):
    # Open the file in binary read and write mode
    with open(path, "ab+") as archivo_ventas:
        # Move the file pointer to the beginning of the file
        archivo_ventas.seek(0)
        # Create a CSV writer object with a comma delimiter
        writer = csv.writer(archivo_ventas, delimiter=',')
        # Write the new row to the CSV file
        writer.writerow(data)
        # Return True to indicate success
        return True

# Function to delete a row from a CSV file based on an ID
def eliminar(path, id):
    # Read the data from the CSV file
    data = leer(path)
    # Iterate over each row in the data
    for i in range(len(data)):
        # Check if the ID in the current row matches the given ID
        if data[i][0] == id:
            # Delete the row from the data list
            del data[i]
            # Break out of the loop
            break
    # Write the updated data back to the CSV file
    escribir(path, data)
    # Return True to indicate success
    return True

def buscar(path,id):
    data=leer(path)
    for row in data:
      if row[0]==id:
       return row
        
