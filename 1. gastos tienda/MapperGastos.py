#!/usr/bin/env python3
import sys

# Mapper para calcular la media gastada por persona y tienda
for linea in sys.stdin:
    # Elimina espacios y separa los campos
    linea = linea.strip()
    persona, tienda, gasto = linea.split(";")

    # Emite la clave (persona;tienda) y el gasto
    print(f"{persona};{tienda}\t{gasto}")

