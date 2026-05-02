# =========================================================
# IMPORTACIÓN DEL MÓDULO CSV
# =========================================================

# El módulo csv permite:
# - leer archivos CSV
# - escribir archivos CSV
#
# CSV significa:
# Comma Separated Values
#
# Ejemplo de CSV:
#
# Book,Sales
# Harry Potter,120
# LOTR,150
#
import csv


# =========================================================
# VARIABLES DE CONTROL
# =========================================================

# max_sales
#
# Guardará el valor MÁS ALTO encontrado durante el recorrido.
#
# Comienza en 0 porque todavía no hemos leído ningún libro.
max_sales = 0


# name_bestseller
#
# Guardará el nombre del libro con más ventas.
#
# Se inicia en None porque aún no conocemos
# cuál es el bestseller.
name_bestseller = None


# =========================================================
# ABRIR EL ARCHIVO CSV EN MODO LECTURA
# =========================================================

# open(..., 'r')
#
# 'r' significa READ (lectura).
#
# encoding='utf8'
#
# Permite leer correctamente caracteres especiales
# como:
# á, é, ñ, etc.
#
# with open(...)
#
# Abre el archivo de forma segura y lo cierra
# automáticamente al terminar.
with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:

    # =====================================================
    # CREAR EL LECTOR CSV
    # =====================================================

    # csv.reader(file)
    #
    # Convierte el archivo CSV en un objeto iterable.
    #
    # Cada fila se convierte en una LISTA.
    #
    # Ejemplo:
    #
    # ['Harry Potter', 'J.K Rowling', '120']
    #
    csv_reader = csv.reader(file)

    # =====================================================
    # SALTAR LA PRIMERA FILA (ENCABEZADOS)
    # =====================================================

    # next(csv_reader)
    #
    # Avanza una fila en el archivo.
    #
    # Esto se usa para ignorar encabezados como:
    #
    # Book,Author,Sales
    #
    next(csv_reader)

    # =====================================================
    # RECORRER CADA FILA DEL CSV
    # =====================================================

    # row representa una fila completa del CSV.
    #
    # Ejemplo:
    #
    # ['Harry Potter', 'J.K Rowling', '120']
    #
    for row in csv_reader:

        # =================================================
        # EXTRAER DATOS DE LA FILA
        # =================================================

        # row[4]
        #
        # Accede a la quinta columna.
        #
        # Aquí se encuentran las ventas.
        sales = row[4]

        # row[0]
        #
        # Accede a la primera columna.
        #
        # Aquí se encuentra el nombre del libro.
        book_name = row[0]

        # =================================================
        # CONVERTIR TEXTO A NÚMERO
        # =================================================

        # Los datos CSV llegan como STRING (texto).
        #
        # Ejemplo:
        #
        # '120'
        #
        # Para comparar correctamente necesitamos
        # convertir el texto a número.
        #
        # float(...)
        #
        # Convierte el valor a decimal.
        sales = float(sales)

        # =================================================
        # COMPARAR VENTAS
        # =================================================

        # Pregunta:
        #
        # ¿Las ventas actuales son mayores
        # que el récord guardado?
        #
        if sales > max_sales:

            # =============================================
            # ACTUALIZAR NUEVO RÉCORD
            # =============================================

            # Guardamos las nuevas ventas máximas.
            max_sales = sales

            # Guardamos el nombre del libro ganador.
            name_bestseller = book_name

    # =====================================================
    # MOSTRAR RESULTADO FINAL
    # =====================================================

    # Este print está fuera del for.
    #
    # Eso significa:
    #
    # "espera a terminar TODO el recorrido
    # antes de mostrar el resultado"
    #
    print('BestSeller:', name_bestseller, max_sales)


# =========================================================
# CREAR NUEVO ARCHIVO CSV
# =========================================================

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
# Evita líneas vacías extra en archivos CSV.
with open('output.csv', 'w', newline='') as file:

    # =====================================================
    # CREAR OBJETO WRITER
    # =====================================================

    # csv.writer(file)
    #
    # Permite escribir filas dentro del CSV.
    csv_writer = csv.writer(file)

    # =====================================================
    # ESCRIBIR FILA EN EL NUEVO CSV
    # =====================================================

    # writerow([...])
    #
    # Escribe UNA FILA dentro del archivo CSV.
    #
    # IMPORTANTE:
    # writerow() recibe UNA LISTA.
    #
    # La lista representa:
    #
    # [columna1, columna2, columna3]
    #
    csv_writer.writerow([name_bestseller, max_sales])