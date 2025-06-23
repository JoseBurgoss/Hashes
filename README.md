# Hash Function Evaluation and Visualization / Evaluación y Visualización de Funciones Hash

## English

### Overview
This repository contains two Python scripts that work together to evaluate and visualize the performance of cryptographic hash functions (MD5, SHA-1, SHA-256) against partial preimage attacks.

### Files Description

#### `hashes.py`
The main evaluation script that performs brute-force searches to find messages whose hash outputs begin with specified hexadecimal zero prefixes. [2](#0-1) 

**Key Components:**
- **Hash Functions**: MD5, SHA-1, SHA-256 [3](#0-2) 
- **Target Prefixes**: "0", "00", "000", "0000" [4](#0-3) 
- **Base Message**: "jose andres burgos bolivar" [5](#0-4)


The script will display a table on screen like this:

```
📊 Resultados finales:
Algoritmo Prefijo Mensaje                        Intentos   Tiempo (s)
MD5      000     jose andres burgos bolivar:3497 3497       0.0054
SHA-1    0000    jose andres burgos bolivar:91031 91031      0.0919
...
```


**Algorithm**: The script generates messages in the format `"jose andres burgos bolivar:N"` where N is an incrementing counter, then computes hashes until finding one that starts with the target prefix. [6](#0-5) 

#### `gráfica_comparativa.py`
A visualization script that creates a comparative graph showing the execution times for different hash algorithms and prefix lengths.

**Features:**
- Uses matplotlib and pandas for data visualization
- Plots execution time vs prefix length for each hash algorithm
- Saves the graph as "grafica_resultados_jose_burgos.png"

### Usage Instructions

#### Running the Hash Evaluation
```bash
python hashes.py
```

This will:
1. Test all three hash algorithms (MD5, SHA-1, SHA-256)
2. For each algorithm, find messages with prefixes "0", "00", "000", "0000"
3. Display progress and final results in a formatted table [7](#0-6) 

#### Generating the Visualization
```bash
python gráfica_comparativa.py
```

This will:
1. Create a line graph comparing execution times
2. Save the graph as "grafica_resultados_jose_burgos.png"
3. Display the graph on screen

### Requirements
- Python 3.6+
- For `hashes.py`: No additional dependencies (uses standard library)
- For `gráfica_comparativa.py`: matplotlib, pandas

### Installation
```bash
pip install matplotlib pandas
```

## Notes

The `gráfica_comparativa.py` script contains hardcoded timing data that should be updated with actual results from running `hashes.py`.  The current data in the visualization script appears to be sample results from a previous execution.  For accurate visualization, you should replace the `datos` array in `gráfica_comparativa.py` with the actual timing results from your `hashes.py` execution. 

## 📈 What can you do with the results?

* Use them for comparative analysis between hash algorithms.
* Build graphs (with Excel or Python) to visualize complexity.
* Include them in academic reports or research articles about cryptography.

---

## 👨‍🎓 Author

José Andrés Burgos Bolívar
Project for the subject *Cryptography and Network Security*

---

## 📄 License

This project is for academic use. You can use it as a base for your own tests and experiments.

---

## Español

### Descripción General
Este repositorio contiene dos scripts de Python que trabajan juntos para evaluar y visualizar el rendimiento de funciones hash criptográficas (MD5, SHA-1, SHA-256) contra ataques de preimagen parcial.

### Descripción de Archivos

#### `hashes.py`
El script principal de evaluación que realiza búsquedas de fuerza bruta para encontrar mensajes cuyos hash comiencen con prefijos específicos de ceros hexadecimales. [1](#0-0) 

**Componentes Clave:**
- **Funciones Hash**: MD5, SHA-1, SHA-256 [3](#0-2) 
- **Prefijos Objetivo**: "0", "00", "000", "0000" [4](#0-3) 
- **Mensaje Base**: "jose andres burgos bolivar" [5](#0-4)

El script mostrará por pantalla una tabla como esta:

```
📊 Resultados finales:
Algoritmo Prefijo Mensaje                        Intentos   Tiempo (s)
MD5      000     jose andres burgos bolivar:3497 3497       0.0054
SHA-1    0000    jose andres burgos bolivar:91031 91031      0.0919
...
``` 

**Algoritmo**: El script genera mensajes en el formato `"jose andres burgos bolivar:N"` donde N es un contador incremental, luego calcula hashes hasta encontrar uno que comience con el prefijo objetivo. [6](#0-5) 

#### `gráfica_comparativa.py`
Un script de visualización que crea un gráfico comparativo mostrando los tiempos de ejecución para diferentes algoritmos hash y longitudes de prefijo.

**Características:**
- Usa matplotlib y pandas para visualización de datos
- Grafica tiempo de ejecución vs longitud de prefijo para cada algoritmo hash
- Guarda el gráfico como "grafica_resultados_jose_burgos.png"

### Instrucciones de Uso

#### Ejecutar la Evaluación de Hash
```bash
python hashes.py
```

Esto:
1. Probará los tres algoritmos hash (MD5, SHA-1, SHA-256)
2. Para cada algoritmo, encontrará mensajes con prefijos "0", "00", "000", "0000"
3. Mostrará el progreso y resultados finales en una tabla formateada [7](#0-6) 

#### Generar la Visualización
```bash
python gráfica_comparativa.py
```

Esto:
1. Creará un gráfico de líneas comparando tiempos de ejecución
2. Guardará el gráfico como "grafica_resultados_jose_burgos.png"
3. Mostrará el gráfico en pantalla

### Requisitos
- Python 3.6+
- Para `hashes.py`: Sin dependencias adicionales (usa biblioteca estándar)
- Para `gráfica_comparativa.py`: matplotlib, pandas

### Instalación
```bash
pip install matplotlib pandas
```

### Flujo de Trabajo Recomendado
1. Ejecutar `python hashes.py` para generar los datos de rendimiento
2. Actualizar los datos en `gráfica_comparativa.py` con los resultados obtenidos
3. Ejecutar `python gráfica_comparativa.py` para generar la visualización

---

## Notas

El script gráfica_comparativa.py contiene datos de tiempo codificados de forma fija que deben actualizarse con los resultados reales de ejecutar hashes.py. Los datos actuales en el script de visualización parecen ser resultados de muestra de una ejecución anterior. Para una visualización precisa, debes reemplazar el array datos en gráfica_comparativa.py con los resultados de tiempo reales de tu ejecución de hashes.py.

---

## 📈 ¿Qué puedes hacer con los resultados?

* Usarlos para análisis comparativo entre algoritmos hash.
* Construir gráficas (con Excel o Python) para visualizar la complejidad.
* Incluirlos en informes académicos o artículos de investigación sobre criptografía.

---

## 👨‍🎓 Autor

José Andrés Burgos Bolívar
Proyecto para la materia *Criptografía y Seguridad de Redes*

---

## 📄 Licencia

Este proyecto es de uso académico. Puedes usarlo como base para tus propias pruebas y experimentos.

## GRAPH EXAMPLE/EJEMPLO DE GRAFICA

![Grafica_Comparativa](https://github.com/user-attachments/assets/23196ca8-54c4-4a75-a103-676555e247c7)
