from algo1 import *

def listadoDecreciente(inicio):
  posicion=0
  if(inicio>50):
    for x in range(inicio,-1,-5):
      posicion=posicion+1
      print(posicion,": ",x)
  else:
    for x in range(inicio,-1,-2):
      posicion=posicion+1
      print(posicion,": ",x)


num1=input_int("Ingrese un número entero: ")
num2=input_int("Ingrese otro número entero para sumarlos: ")
suma=num1+num2

lista=listadoDecreciente(suma)
