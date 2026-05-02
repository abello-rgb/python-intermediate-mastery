# =========================================================
# SIMULACIÓN DE "ELIMINAR" O "DESENVIAR" UN MENSAJE
# =========================================================

# Variable que almacena el mensaje original.
# Es simplemente un texto guardado en memoria.
sent_message = 'Hey there! This is a secret message.'


# =========================================================
# PASO 1: CREAR EL ARCHIVO Y GUARDAR EL MENSAJE
# =========================================================

# open('send_message.txt', 'w')
#
# 'w' significa WRITE (escritura).
# Este modo:
#   - Crea el archivo si no existe.
#   - Borra TODO el contenido si ya existía.
#
# "with" se usa para abrir archivos de forma segura.
# Cuando el bloque termina, Python cierra el archivo automáticamente.
with open('send_message.txt', 'w') as file:

    # file.write(...)
    #
    # Escribe el contenido dentro del archivo.
    file.write(sent_message)


# =========================================================
# PASO 2: ABRIR EL ARCHIVO PARA LEER Y MODIFICAR
# =========================================================

# 'r+' significa:
#   r  -> read  (leer)
#   +  -> también permite escribir
#
# Entonces:
#   - puedes LEER el archivo
#   - y también MODIFICARLO
with open('send_message.txt', 'r+') as file:

    # file.read()
    #
    # Lee TODO el contenido del archivo.
    # El texto leído se guarda en la variable original_message.
    original_message = file.read()

    # file.seek(0)
    #
    # Mueve el cursor al inicio del archivo.
    #
    # IMPORTANTE:
    # Los archivos tienen un "cursor" interno que indica
    # en qué posición estás leyendo o escribiendo.
    #
    # Después de read(), el cursor queda al FINAL del archivo.
    # Por eso debemos volver al inicio con seek(0).
    file.seek(0)

    # =====================================================
    # NUEVO MENSAJE QUE REEMPLAZARÁ EL ORIGINAL
    # =====================================================

    # Simulación de "mensaje eliminado"
    unsent_message = 'This message has been unsent.'

    # file.truncate(numero)
    #
    # Recorta el tamaño del archivo.
    #
    # Aquí se está diciendo:
    # "Haz que el archivo tenga exactamente
    # la longitud del nuevo mensaje"
    #
    # Esto evita que queden restos del mensaje viejo.
    file.truncate(len(unsent_message))

    # file.write(...)
    #
    # Escribe el nuevo mensaje desde el inicio del archivo.
    file.write(unsent_message)


# =========================================================
# MOSTRAR RESULTADOS EN CONSOLA
# =========================================================

# Muestra el mensaje original que se leyó antes de modificarlo.
print('Original Message:', original_message)

# Muestra el nuevo mensaje escrito en el archivo.
print('Unsent Message:', unsent_message)