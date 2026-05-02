# =========================================================
# FUNCIONES DE ORDEN SUPERIOR Y CLOSURES
# =========================================================

# Este ejercicio utiliza:
#
# - funciones internas
# - funciones retornando funciones
# - closures
# - diccionarios anidados
#
# El objetivo es crear traductores especializados
# para diferentes idiomas.
#
# =========================================================
# FUNCIÓN EXTERIOR
# =========================================================

def translator(language):

    # =====================================================
    # DICCIONARIO DE TRADUCCIONES
    # =====================================================

    # translations contiene varios idiomas.
    #
    # Cada idioma tiene:
    # - palabras clave
    # - traducciones asociadas
    #
    # Estructura:
    #
    # {
    #   idioma: {
    #       palabra_original: traduccion
    #   }
    # }
    #
    translations = {

        'spanish': {
            'hello': 'hola',
            'goodbye': 'adiós',
            'thank you': 'gracias'
        },

        'french': {
            'hello': 'bonjour',
            'goodbye': 'au revoir',
            'thank you': 'merci'
        },

        'italian': {
            'hello': 'ciao',
            'goodbye': 'arrivederci',
            'thank you': 'grazie'
        }
    }

    # =====================================================
    # FUNCIÓN INTERNA
    # =====================================================

    # Esta función recibe una palabra y devuelve
    # su traducción según el idioma seleccionado.
    #
    # IMPORTANTE:
    #
    # La función puede acceder a:
    #
    # language
    #
    # aunque NO fue pasado como parámetro.
    #
    # Esto ocurre gracias a un CLOSURE.
    #
    def translate_word(word):

        # ================================================
        # ACCESO DINÁMICO AL DICCIONARIO
        # ================================================

        # translations[language]
        #
        # Accede al idioma seleccionado.
        #
        # Ejemplo:
        #
        # translations['spanish']
        #
        # devuelve:
        #
        # {
        #   'hello': 'hola',
        #   ...
        # }
        #
        # Luego:
        #
        # [word]
        #
        # accede a la palabra específica.
        #
        # Ejemplo:
        #
        # translations['spanish']['hello']
        #
        # devuelve:
        #
        # 'hola'
        #
        return translations[language][word]

    # =====================================================
    # RETORNAR LA FUNCIÓN INTERNA
    # =====================================================

    # IMPORTANTE:
    #
    # NO usamos:
    #
    # translate_word()
    #
    # porque eso EJECUTARÍA la función.
    #
    # Queremos retornar la FUNCIÓN en sí.
    #
    return translate_word


# =========================================================
# CREAR TRADUCTOR ESPECIALIZADO
# =========================================================

# translator('spanish')
#
# NO traduce todavía.
#
# Lo que hace es:
#
# crear una función especializada en español.
#
translate_to_spanish = translator('spanish')


# =========================================================
# USAR LA FUNCIÓN RETORNADA
# =========================================================

# Ahora:
#
# translate_to_spanish
#
# contiene la función interna:
#
# translate_word()
#
# Entonces podemos ejecutarla como cualquier función.
#
translated_word = translate_to_spanish('hello')


# =========================================================
# MOSTRAR RESULTADO
# =========================================================

print('Translated Word:', translated_word)