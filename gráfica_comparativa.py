import matplotlib.pyplot as plt
import pandas as pd

datos = [
    {"Algoritmo": "MD5", "Prefijo": "0", "Tiempo (s)": 0.0000},
    {"Algoritmo": "MD5", "Prefijo": "00", "Tiempo (s)": 0.0000},
    {"Algoritmo": "MD5", "Prefijo": "000", "Tiempo (s)": 0.0054},
    {"Algoritmo": "MD5", "Prefijo": "0000", "Tiempo (s)": 0.0748},
    {"Algoritmo": "SHA-1", "Prefijo": "0", "Tiempo (s)": 0.0000},
    {"Algoritmo": "SHA-1", "Prefijo": "00", "Tiempo (s)": 0.0000},
    {"Algoritmo": "SHA-1", "Prefijo": "000", "Tiempo (s)": 0.0032},
    {"Algoritmo": "SHA-1", "Prefijo": "0000", "Tiempo (s)": 0.0919},
    {"Algoritmo": "SHA-256", "Prefijo": "0", "Tiempo (s)": 0.0000},
    {"Algoritmo": "SHA-256", "Prefijo": "00", "Tiempo (s)": 0.0154},
    {"Algoritmo": "SHA-256", "Prefijo": "000", "Tiempo (s)": 0.0030},
    {"Algoritmo": "SHA-256", "Prefijo": "0000", "Tiempo (s)": 0.1156},
]

df = pd.DataFrame(datos)

plt.figure(figsize=(10, 6))
for algoritmo in df['Algoritmo'].unique():
    subset = df[df['Algoritmo'] == algoritmo]
    plt.plot(subset['Prefijo'], subset['Tiempo (s)'], marker='o', label=algoritmo)

plt.title("Comparación de Tiempo vs Prefijo en Funciones Hash")
plt.xlabel("Prefijo (número de ceros hexadecimales)")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_resultados_jose_burgos.png")
plt.show()
