# programa para verficar si un numero es par

#input
print("-------------------------------")
print("--------Número par/impar--------")
print("-------------------------------")
min= int(input("digite un número: "))

#prosecing
mod = x%2
if (mod == 0):
    rta = "PAR"
else:
    rta = "IMPAR"

#output
print("--------------------------")
print("---------Resultado--------")
print("--------------------------")
print("El número " + str(x) + " es " + rta)