def run1():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(mi_diccionario)  # {'llave1': 1, 'llave2': 2, 'llave3': 3}
    print(mi_diccionario['llave1'])  # 1
    print(mi_diccionario['llave2'])  # 2
    print(mi_diccionario['llave3'])  # 3


def run2():
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }
    print(poblacion_paises['Argentina'])  # 44938712
    print(poblacion_paises['Bolivia'])  # Error (KeyError)
    print(poblacion_paises.keys())  # dict_keys(['Argentina', 'Brasil', 'Colombia'])
    for pais in poblacion_paises.keys():
        print(pais)  # Argentina, Brasil, Colombia

    print(poblacion_paises.values())  # dict_values([44938712, 210147125, 50372424])
    for poblacion in poblacion_paises.values():
        print(poblacion)  # 44938712, 210147125, 50372424

    print(poblacion_paises.items())
    # dict_items([('Argentina', 44938712), ('Brasil', 210147125), ('Colombia', 50372424)])
    for poblacion in poblacion_paises.items():
        print(poblacion)  # ('Argentina', 44938712), ('Brasil', 210147125), ('Colombia', 50372424)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run2()
