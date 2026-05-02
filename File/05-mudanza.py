# =========================================================
# IMPORTAR EL MÓDULO CSV
# =========================================================

# El módulo csv permite trabajar con archivos CSV.
#
# CSV significa:
# Comma Separated Values
#
# Ejemplo:
#
# Item,Quantity
# Blender,2
# Posters,30
#
import csv


# =========================================================
# DATOS QUE SE ESCRIBIRÁN EN EL CSV
# =========================================================

# data es una lista que contiene múltiples filas.
#
# Cada lista interna representa UNA FILA del archivo CSV.
#
# Ejemplo:
#
# ['Blender', 2]
#
# se convertirá en:
#
# Blender,2
#
data = [

    # Encabezados del CSV
    ['Item', 'Quantity'],

    # Filas de datos
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]


# =========================================================
# BLOQUE TRY
# =========================================================

# try:
#
# Intenta ejecutar el código.
#
# Si ocurre un error:
# Python saltará automáticamente al bloque except.
#
try:

    # =====================================================
    # ABRIR ARCHIVO CSV EN MODO LECTURA
    # =====================================================

    # open(..., 'r')
    #
    # 'r' significa READ (lectura).
    #
    # encoding='utf8'
    #
    # Permite manejar caracteres especiales correctamente.
    #
    # with open(...)
    #
    # Abre el archivo de forma segura y lo cierra
    # automáticamente al terminar.
    #
    with open('packing_list.csv', 'r', encoding='utf8') as file:

        # =================================================
        # CREAR OBJETO READER
        # =================================================

        # csv.reader(file)
        #
        # Convierte el archivo CSV en un objeto iterable.
        #
        # Cada fila del CSV se transforma en una lista.
        #
        # Ejemplo:
        #
        # ['Blender', '2']
        #
        csv_reader = csv.reader(file)

        # =================================================
        # RECORRER FILAS DEL CSV
        # =================================================

        # row representa UNA FILA del archivo CSV.
        #
        # Ejemplo:
        #
        # ['Posters', '30']
        #
        for row in csv_reader:

            # Mostrar cada fila en consola
            print(row)


# =========================================================
# BLOQUE EXCEPT
# =========================================================

# except FileNotFoundError:
#
# Este bloque se ejecuta SOLO si el archivo
# no existe.
#
# FileNotFoundError significa:
#
# "Python no encontró el archivo solicitado"
#
except FileNotFoundError:

    # =====================================================
    # CREAR NUEVO ARCHIVO CSV
    # =====================================================

    # open(..., 'w')
    #
    # 'w' significa WRITE (escritura).
    #
    # Si el archivo no existe:
    # → lo crea
    #
    # Si ya existe:
    # → sobrescribe el contenido
    #
    # newline=''
    #
    # Evita líneas vacías adicionales
    # al escribir archivos CSV.
    #
    with open('packing_list.csv', 'w', newline='', encoding='utf8') as file:

        # ================================================
        # CREAR OBJETO WRITER
        # ================================================

        # csv.writer(file)
        #
        # Permite escribir datos dentro del CSV.
        #
        csv_writer = csv.writer(file)

        # ================================================
        # ESCRIBIR MÚLTIPLES FILAS
        # ================================================

        # writerows(data)
        #
        # Escribe MUCHAS filas a la vez.
        #
        # IMPORTANTE:
        #
        # writerows() recibe:
        #
        # una lista que contiene múltiples listas.
        #
        # Ejemplo:
        #
        # [
        #   ['Item', 'Quantity'],
        #   ['Blender', 2]
        # ]
        #
        csv_writer.writerows(data)


# =========================================================
# BLOQUE FINALLY
# =========================================================

# finally:
#
# Este bloque SIEMPRE se ejecuta:
#
# - haya errores o no
# - exista el archivo o no
#
# Se usa comúnmente para:
# - cerrar recursos
# - mostrar mensajes finales
# - limpiar procesos
#
finally:

    print('Fin del programa')