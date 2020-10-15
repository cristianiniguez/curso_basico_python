def run1():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)


def run2():
    for i in range(10000):
        print(i)
        if i == 5678:
            break


def run3():
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


def run4():
    LIMITE = 10
    donas = 0
    while donas < LIMITE:
        pedido = int(input('¿Cuántas donas quieres?: '))
        if pedido == 0:
            print('¿Ya no quieres? Bueno adiós')
            break
        donas += pedido
        print('Ahora tienes ' + str(donas) + ' dona(s)')


if __name__ == '__main__':
    run4()
