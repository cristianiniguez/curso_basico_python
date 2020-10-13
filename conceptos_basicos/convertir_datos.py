numero1 = input("Escribe un número: ")
# Escribe un número: 4 (este 4 lo está poniendo el usuario)
numero1 # '4' (es un texto por las comillas)

numero2 = input("Escribe un número: ")
# Escribe un número: 5
numero2 # '5'
numero1 + numero2 # '45' (no es 9 por que son textos y por lo tanto se concatenan)

numero1 = int(numero1)
numero1 # 4 (ya es un número)

numero2 = int(numero2)
numero2 # 5

numero1 + numero2 # 9 (ya se sumaron)

numero_decimal = 4.5
int(numero_decimal) # 4
str(numero_decimal) # '4.5'
