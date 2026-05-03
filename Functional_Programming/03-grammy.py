# Grammys 🏆
# Codédex
# Título/comentario del ejercicio.

from functools import reduce
# Importamos reduce desde functools porque en Python no está disponible
# directamente como función integrada.

playlist = [
  ('What Was I Made For?', 3.42), 
  ('Just Like That', 5.05), 
  ('Song 3', 6.55), 
  ('Leave The Door Open', 4.02), 
  ('I Can\'t Breath', 4.47), 
  ('Bad Guy', 3.14)
]
# Creamos una lista llamada playlist.
# Cada elemento es una tupla con:
# - posición 0: nombre de la canción
# - posición 1: duración de la canción


def longer_than_five_minutes(song):
  return song[1] > 5.00
# Esta función recibe una canción completa (una tupla).
# song[1] accede a la duración.
# Devuelve True si dura más de 5 minutos, y False si no.
# Esta función será usada por filter().


def minutes_to_seconds(song):
  duration = song[1]
  # Guardamos la duración de la canción en una variable.

  minutes = int(duration)
  # Extraemos la parte entera del número.
  # Ejemplo: si duration es 3.42, minutes será 3.

  seconds = (duration - minutes) * 100
  # Tomamos la parte decimal y la convertimos en segundos.
  # Ejemplo: 3.42 - 3 = 0.42, luego 0.42 * 100 = 42.

  return minutes * 60 + round(seconds)
  # Convertimos los minutos a segundos y sumamos los segundos restantes.
  # Ejemplo: 3 minutos = 180 segundos, más 42 = 222.
  # Esta función será usada por map().


def add_durations(total, song):
  duration = song[1]
  # Extraemos la duración de la canción actual.

  return total + duration
  # Sumamos la duración de la canción al acumulado total.
  # Esta función será usada por reduce().


filtered_songs = list(filter(longer_than_five_minutes, playlist))
# filter() recorre playlist y conserva solo las canciones
# para las que longer_than_five_minutes(song) devuelve True.
# list() convierte el resultado en una lista normal.


convert_to_seconds = list(map(minutes_to_seconds, playlist))
# map() recorre playlist y aplica minutes_to_seconds(song)
# a cada canción.
# El resultado es una lista con las duraciones convertidas a segundos.


total_playtime = reduce(add_durations, playlist, 0)
# reduce() recorre playlist y va acumulando un único valor.
# Empieza en 0 y, en cada paso, add_durations(total, song)
# suma la duración de la canción actual al total acumulado.


print(filtered_songs) 
# Imprime las canciones que duran más de 5 minutos.

print(convert_to_seconds)
# Imprime la lista de duraciones convertidas a segundos.

print(total_playtime)
# Imprime la suma total de las duraciones del playlist.