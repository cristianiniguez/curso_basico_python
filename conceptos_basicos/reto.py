# Conversor de dólares a pesos bolivianos

dolares = input('¿Cuántos dólares tienes?: ')
dolares = float(dolares)
valor_dolar = 6.91
pesos = dolares * valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print('Tienes BS ' + pesos + ' pesos bolivianos')
