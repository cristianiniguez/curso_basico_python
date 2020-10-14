nombre = input('¿Cuál es tu nombre?: ') # 'cristian '
nombre # 'cristian '
nombre.upper() # 'CRISTIAN '
nombre.capitalize() # 'Cristian '

nombre = nombre.capitalize()
nombre # 'Cristian '

nombre = nombre.strip()
nombre # 'Cristian' (sin espacio al principio o al final)

nombre.lower() # 'cristian'
nombre.replace('a', 'o') # 'Cristion'
nombre[0] # 'C'
nombre[1] # 'r'

letra = nombre[2]
letra # 'i'

len(nombre) # 8
len(letra) # 1
len('Hola! Este es el curso de python') # 32
