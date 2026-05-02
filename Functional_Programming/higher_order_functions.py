# =========================================================
# FUNCIONES DE ORDEN SUPERIOR (HIGHER-ORDER FUNCTIONS)
# =========================================================

# Una función de orden superior es una función que:
#
# 1. Recibe otras funciones como argumento
# o
# 2. Retorna funciones
#
# En este ejemplo:
#
# apply_operation()
#
# recibe otra función llamada:
#
# triple
#
# 🔥 Eso la convierte en una función de orden superior.


# =========================================================
# FUNCIÓN DE ORDEN SUPERIOR
# =========================================================

def apply_operation(operation, numbers):

    # ================================================
    # LISTA DONDE SE GUARDARÁN LOS NUEVOS RESULTADOS
    # ================================================

    # result almacenará los números transformados.
    #
    # Ejemplo final:
    #
    # [3, 6, 9, 12, 15, 18]
    #
    result = []

    # ================================================
    # RECORRER CADA NÚMERO DE LA LISTA
    # ================================================

    # num representa un elemento individual de numbers.
    #
    # Ejemplo:
    #
    # Primera vuelta:
    # num = 1
    #
    # Segunda vuelta:
    # num = 2
    #
    for num in numbers:

        # ============================================
        # EJECUTAR LA FUNCIÓN RECIBIDA
        # ============================================

        # operation(num)
        #
        # Aquí ocurre la parte MÁS importante.
        #
        # operation es una FUNCIÓN recibida como parámetro.
        #
        # En este caso:
        #
        # operation = triple
        #
        # Entonces esto realmente ejecuta:
        #
        # triple(num)
        #
        # Ejemplo:
        #
        # triple(1) -> 3
        #
        result.append(operation(num))

    # ================================================
    # RETORNAR NUEVA LISTA TRANSFORMADA
    # ================================================

    return result


# =========================================================
# FUNCIÓN NORMAL
# =========================================================

def triple(x):

    # Multiplica el número por 3.
    return x * 3


# =========================================================
# LISTA ORIGINAL
# =========================================================

numbers_list = [1, 2, 3, 4, 5, 6]


# =========================================================
# USAR FUNCIÓN DE ORDEN SUPERIOR
# =========================================================

# Aquí pasamos:
#
# triple
#
# como argumento.
#
# IMPORTANTE:
#
# NO usamos:
#
# triple()
#
# porque eso EJECUTARÍA la función inmediatamente.
#
# Queremos pasar la FUNCIÓN en sí.
#
triple_numbers = apply_operation(triple, numbers_list)


# =========================================================
# MOSTRAR RESULTADOS
# =========================================================

print('Original Numbers:', numbers_list)

# Nota:
# El texto dice "Doubled Numbers"
# pero realmente estamos triplicando números.
#
# Más correcto sería:
#
# "Tripled Numbers"
#
print('Doubled Numbers:', triple_numbers)