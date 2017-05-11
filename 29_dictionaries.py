#there's no order in dictionaries. only keys, values

exdn = { 'kack':23, 'alice': 24, 23: 'easyman'}

print(exdn['alice'],exdn[23])

exdn['uday']='hero'

print(exdn)

del exdn['alice']
#this deletes 24

print(exdn)
