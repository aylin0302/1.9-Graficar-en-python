#Grafica 1:Relación entre elementos y electronegatividad

import matplotlib.pyplot as plt

# Datos para electronegatividad
elementos = ['H', 'C', 'O', 'N', 'Cl', 'S', 'F', 'P', 'I', 'Br']
electronegatividad = [2.20, 2.55, 3.44, 3.04, 3.16, 2.58, 3.98, 2.19, 2.66, 2.96]

# Gráfico de electronegatividad
plt.figure(figsize=(8, 5))
plt.bar(elementos, electronegatividad, color='skyblue')
plt.title('Relación entre Elementos y Electronegatividad')
plt.xlabel('Elementos')
plt.ylabel('Electronegatividad (Pauling)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Gráfica 2: Relación de elementos y su masa molar 
import matplotlib.pyplot as plt

# Datos: Elementos químicos y sus masas molares (g/mol)
elementos = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
masas_molares = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(elementos, masas_molares, color='skyblue', edgecolor='black')

# Personalización del gráfico
plt.title('Relación entre Elementos y su Masa Molar', fontsize=14)
plt.xlabel('Elementos Químicos', fontsize=12)
plt.ylabel('Masa Molar (g/mol)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Mostrar la gráfica
plt.tight_layout()
plt.show()

#Grafica 3 :Relación de viscosidad y temperatura de un Aceite de motor.

import matplotlib.pyplot as plt
import numpy as np

# Datos: Temperatura (°C) y viscosidad (mPa·s) de un aceite de motor
temperaturas = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
viscosidades = [1200, 450, 200, 120, 80, 50, 35, 25, 20, 18]

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar la relación viscosidad-temperatura
ax.plot(temperaturas, viscosidades, marker='o', color='blue', label='Viscosidad vs Temperatura')

# Personalización del gráfico
ax.set_title('Relación entre Viscosidad y Temperatura de un Aceite de Motor', fontsize=14)
ax.set_xlabel('Temperatura (°C)', fontsize=12)
ax.set_ylabel('Viscosidad (mPa·s)', fontsize=12)
ax.grid(alpha=0.5)
ax.legend(fontsize=10)
ax.set_xlim(0, 200)
ax.set_ylim(0, 1300)

# Crear la tabla
column_labels = ['Temperatura (°C)', 'Viscosidad (mPa·s)']
table_data = list(zip(temperaturas, viscosidades))
table = plt.table(cellText=table_data, colLabels=column_labels, cellLoc='center', loc='bottom', bbox=[0.0, -0.4, 1, 0.3])

# Ajustar diseño para la tabla
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(column_labels))))
plt.subplots_adjust(left=0.2, bottom=0.4)

# Mostrar la gráfica y la tabla
plt.show()


