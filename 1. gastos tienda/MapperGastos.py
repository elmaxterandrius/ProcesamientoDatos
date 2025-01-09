#!/usr/bin/python3
import sys

# Creado por Andres Ruiz

# Mapper para calcular la media gastada por persona y tienda
for linea in sys.stdin:
    
    # Elimina espacios y separa los campos
    linea = linea.strip()
    
    #Separa los datos en base al ;
    persona, tienda, gasto = linea.split(";")
    
    # Emite la clave (persona;tienda) y el gasto
    print(f"{persona};{tienda}\t{gasto}")


# Para probar por consola este codigo se lo hace de la siguiente manera

# Cambiar al directorio del codigo MapperGastos
# C:\Users\wilme\OneDrive - Universidad internacional de valencia\0. Materias\2. Obligatorias\3. Procesamiento de datos\3. Tareas\3. MapReduce\desarrollo tarea\ProcesamientoDatos\1. gastos tienda

# Luego colocar 

# echo "Alice;Tienda1;50" | python MapperGastos.py