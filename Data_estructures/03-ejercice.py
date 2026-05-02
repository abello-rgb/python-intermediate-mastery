dictionary_list = [
    {
        'name': 'Carlos Gomez',
        'position': 'Delantero',
        'number_jersey': 15,
        'touchdowns': 54
    },
    {
        'name': 'Luis Fernandez',
        'position': 'Mediocampista',
        'number_jersey': 8,
        'touchdowns': 15
    },
    {
        'name': 'Miguel Alvarez',
        'position': 'Defensa',
        'number_jersey': 5,
        'touchdowns': 44
    },
    {
        'name': 'Javier Lopez',
        'position': 'Portero',
        'number_jersey': 1,
        'touchdowns': 51
    },
    {
        'name': 'Andres Ramirez',
        'position': 'Delantero',
        'number_jersey': 10,
        'touchdowns': 66
    }
]

# Print list
for diccionario in dictionary_list:
    print(diccionario.get('position'))
# Select player

dictionary_list[0]['touchdowns'] = 225
print(dictionary_list)

# 
acum = 0
for diccionario in dictionary_list:
    acum += diccionario['touchdowns'] 

print(f'Total {acum/len(dictionary_list)}')