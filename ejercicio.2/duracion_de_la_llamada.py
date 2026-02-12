# programa para verificar costo de una llamada

#input
print("-------------------------------")
print("--------Costo llamada--------")
print("-------------------------------")
min= int(input("digite la duración de la llamada: "))

#prosecing
if (min <= 3):
    costo llamada = 500
else:
    costo_llamada = 500 + (min - 3)*100

#output
print("--------------------------")
print("---------Resultado--------")
print("--------------------------")
print("duración de la llamada: " + str(min))
print("duración de la llamada: " + str(costo_llamada))