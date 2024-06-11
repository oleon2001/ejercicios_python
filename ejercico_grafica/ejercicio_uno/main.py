import matplotlib.pyplot as plt
import numpy as np

# Define variables
t_inicial = 0  # Initial time point
t_final = 10  # Final time point
t_intervalo = 0.1  # Time interval between each point
tasa_crecimiento = 0.02  # Growth rate of the bacterial population
poblacion_inicial = 100  # Initial population size

# Create time array
tiempo = np.arange(t_inicial, t_final + t_intervalo, t_intervalo)
# Generate an array of evenly spaced values from t_inicial to t_final with a step size of t_intervalo

# Initialize population list
poblacion = [poblacion_inicial]
# Initialize the population list with the initial population size

# Simulate population growth
for t in tiempo[1:]:  # Iterate over the time array, starting from the second element
    poblacion.append(poblacion[-1] * np.exp(tasa_crecimiento * t_intervalo))
    #np.exp(): Es una función de NumPy que calcula la exponencial de un número. En este caso, se utiliza para calcular el factor de crecimiento de la población en el siguiente intervalo de tiempo.
    # Calculate the new population size using the exponential growth formula
    #poblacion[-1] se utiliza para acceder al último elemento de una lista llamada poblacion.
# Create plot
plt.figure()
plt.plot(tiempo, poblacion, label='Crecimiento bacteriano')
# Plot the population size over time with a label
plt.title('Crecimiento exponencial de bacterias')
# Set the title of the plot
plt.xlabel('Tiempo (horas)')
# Set the x-axis label
plt.ylabel('Cantidad de bacterias')
# Set the y-axis label
plt.legend()
# Add a legend to the plot
plt.grid(True)
# Add a grid to the plot

# Show plot
plt.show()
# Display the plot