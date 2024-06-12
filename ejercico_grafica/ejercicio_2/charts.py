import matplotlib.pyplot as plt



def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

# Main function
if __name__ == '__main__':
  # Define the labels for the charts
  labels = ['a', 'b', 'c']
  # Define the values for the charts
  values = [10, 40, 800]
  # Generate a bar chart with the given labels and values
  generate_bar_chart(labels, values)
  # Generate a pie chart with the given labels and values
