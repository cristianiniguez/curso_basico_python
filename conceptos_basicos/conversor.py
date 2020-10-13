# Conversor de pesos bolivianos a dólares

pesos = input('¿Cuántos pesos bolivianos tienes?: ')
pesos = float(pesos)
valor_dolar = 6.91
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $' + dolares + ' dólares')
