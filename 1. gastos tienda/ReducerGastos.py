#!/usr/bin/python3
import sys

# Reducer para calcular el gasto medio por persona y tienda
current_key = None
sum_gasto = 0
count = 0

for linea in sys.stdin:
    # Divide la línea en clave y valor
    linea = linea.strip()
    key, gasto = linea.split("\t")
    gasto = float(gasto)

    # Si estamos procesando una nueva clave
    if current_key != key:
        if current_key is not None:
            # Emite la clave anterior y el gasto medio
            persona, tienda = current_key.split(";")
            print(f"{persona};{tienda};{sum_gasto / count:.2f}")

        # Actualiza para la nueva clave
        current_key = key
        sum_gasto = gasto
        count = 1
    else:
        # Acumula los valores para la clave actual
        sum_gasto += gasto
        count += 1

# Emite la última clave procesada
if current_key is not None:
    persona, tienda = current_key.split(";")
    print(f"{persona};{tienda};{sum_gasto / count:.2f}")
