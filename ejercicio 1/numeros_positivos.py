# programa para verificar si un numero es positivo

#input
print("-------------------------------")
print("--------Numero positivo--------")
print("-------------------------------")
x = int(input("digite un numero: "))

#prosecing
if (x>0):
    rta = "POSITIVO"
else:
    rta = "NEGATIVO O CERO"

#output
print("--------------------------")
print("---------Resultado--------")
print("--------------------------")
pint("El número" + str(x) + " es " + rta)