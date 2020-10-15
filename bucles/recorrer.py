def run1():
    nombre = input('Escribe tu nombre: ')
    for letra in nombre:
        print(letra)


def run2():
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run2()
