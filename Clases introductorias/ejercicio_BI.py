#Levanto las librerias
import matplotlib.pyplot as plt
import numpy as np

# Datos inventados
edades = ['0-10', '11-18', '19-30', '31-50', '51-65', '66-80']
padres = [90, 50, 30, 20, 10, 0]
amigos = [10, 40, 50, 30, 20, 10]
trabajo = [0, 10, 30, 50, 50, 10]
familias = [90, 60, 40, 50, 40, 20]

x = np.arange(len(edades))
width = 0.2

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(12, 7))

# Graficar datos
rects1 = ax.bar(x - 1.5*width, padres, width, label='Padres')
rects2 = ax.bar(x - 0.5*width, amigos, width, label='Amigos')
rects3 = ax.bar(x + 0.5*width, trabajo, width, label='Compañeros de trabajo')
rects4 = ax.bar(x + 1.5*width, familias, width, label='Familias')

# Añadir etiquetas
ax.set_xlabel('Edad (años)')
ax.set_ylabel('Porcentaje del tiempo')
ax.set_title('Distribución del tiempo entre padres, amigos, compañeros de trabajo y familias')
ax.set_xticks(x)
ax.set_xticklabels(edades)
ax.legend()

# Añadir valor encima de cada barra
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.tight_layout()
plt.show()
