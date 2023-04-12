from algo1 import *

def num_menor(numeros,menor):
  for x in range(0,3):
    if (numeros[x]<menor):
      menor=numeros[x]
  return menor

def num_mayor(numeros,mayor):
  for x in range(0,3):
    if (numeros[x]>mayor):
      mayor=numeros[x]
  return mayor

def promedio_extremos(menor,mayor):
  promedio=(menor+mayor)/2
  return promedio

numeros=Array(3,0.0)
lista=Array(3,0.0)
menor=0;mayor=0

print("Ingrese 3 números reales")
for x in range(0,3):
  numeros[x]=input_real("")
  menor=menor+numeros[x]
  mayor=mayor-numeros[x]

menor=num_menor(numeros,menor)
mayor=num_mayor(numeros,mayor)

lista[0]=menor;lista[2]=mayor
for x in range (0,3):
  if(numeros[x]!=menor)and(numeros[x]!=mayor):
    lista[1]=numeros[x]
print("Los números ordenados de menor a mayor: ",lista)

promedio=promedio_extremos(menor,mayor)
print("El promedio de sus extremos es: ",promedio)