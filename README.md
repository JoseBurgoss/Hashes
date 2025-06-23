```markdown
# 🔐 Evaluación de Preimágenes Parciales en Funciones Hash

Este proyecto tiene como objetivo evaluar la resistencia de tres funciones hash criptográficas (MD5, SHA-1 y SHA-256) ante la búsqueda de preimágenes parciales mediante fuerza bruta.

## 🧪 ¿Qué hace este programa?

El script genera mensajes con el formato:

```

jose andres burgos bolivar:<contador>

````

y aplica funciones hash para encontrar mensajes cuyo **hash comience con un número creciente de ceros hexadecimales** (`0`, `00`, `000`, `0000`). Se mide el número de intentos y el tiempo requerido para cada caso y algoritmo.

---

## 📁 Estructura del proyecto

- `hashes.py` → Script principal que ejecuta el experimento.
- `README.md` → Este archivo con instrucciones.

---

## ⚙️ Requisitos

- Python 3.6 o superior
- No requiere librerías externas (usa solo la librería estándar `hashlib` y `time`).

---

## ▶️ Cómo ejecutar el código

### 1. Clona este repositorio o descarga el archivo

```bash
git clone https://github.com/tu-usuario/hash.git
cd hash
````

O simplemente descarga `hashes.py` desde GitHub.

---

### 2. Ejecuta el script

Desde una terminal, corre el siguiente comando:

```bash
python hashes.py
```

> Asegúrate de tener Python instalado y agregado a tu PATH.

---

### 3. Observa los resultados

El script mostrará por pantalla una tabla como esta:

```
📊 Resultados finales:
Algoritmo Prefijo Mensaje                        Intentos   Tiempo (s)
MD5      000     jose andres burgos bolivar:3497 3497       0.0054
SHA-1    0000    jose andres burgos bolivar:91031 91031      0.0919
...
```

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

```
