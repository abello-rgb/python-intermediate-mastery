
artefac_info = {
    'artist':'Louis C. Tiffany',
    'period':'ca',
    'date':194
}


print(artefac_info)
print('Keys:', artefac_info.keys())
print('Values:', artefac_info.values())



for key in artefac_info.keys():
    print(key)

for value in artefac_info.values():
    print(value)

for key, value in artefac_info.items():
    print('Key:', key, 'Value:', value)