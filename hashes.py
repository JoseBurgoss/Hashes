import hashlib
import time

NOMBRE_COMPLETO = "jose andres burgos bolivar"

HASH_FUNCTIONS = {
    'MD5': hashlib.md5,
    'SHA-1': hashlib.sha1,
    'SHA-256': hashlib.sha256
}

PREFIXES = ["0", "00", "000", "0000"]

resultados = []

def buscar_hash_con_prefijo(hash_name, hash_func, prefix):
    contador = 0
    inicio = time.time()

    while True:
        mensaje = f"{NOMBRE_COMPLETO}:{contador}"
        hash_resultado = hash_func(mensaje.encode()).hexdigest()
        if hash_resultado.startswith(prefix):
            fin = time.time()
            duracion = fin - inicio
            return {
                "Algoritmo": hash_name,
                "Prefijo": prefix,
                "Mensaje": mensaje,
                "Hash": hash_resultado,
                "Intentos": contador,
                "Tiempo (s)": round(duracion, 4)
            }
        contador += 1

for hash_name, hash_func in HASH_FUNCTIONS.items():
    print(f"\nEjecutando pruebas para {hash_name}...")
    for prefix in PREFIXES:
        resultado = buscar_hash_con_prefijo(hash_name, hash_func, prefix)
        resultados.append(resultado)
        print(f"{hash_name} con prefijo '{prefix}': encontrado en {resultado['Intentos']} intentos y {resultado['Tiempo (s)']} segundos")

print("\nResultados finales:")
print("{:<8} {:<6} {:<30} {:<10} {:<10}".format("Algoritmo", "Prefijo", "Mensaje", "Intentos", "Tiempo (s)"))
for r in resultados:
    print("{:<8} {:<6} {:<30} {:<10} {:<10}".format(
        r["Algoritmo"], r["Prefijo"], r["Mensaje"], r["Intentos"], r["Tiempo (s)"]
    ))
