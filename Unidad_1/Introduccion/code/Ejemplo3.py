from algo1 import *

def calcula_media(desde, hasta):
  suma=0
  cantidad=0
  for x in range(desde,hasta+1):
    suma=suma+x
    cantidad=cantidad+1
  media= suma/cantidad
  return media

entero1=input_int("Ingrese el valor desde: ")
entero2=input_int("Ingrese el valor hasta: ")

promedio=calcula_media(entero1,entero2)
print("El promedio es: ",promedio)