from algo1 import *

sumaimpares=0
sumapares=0

for n in range(1,100):
  if(n%2 == 0):
    #print(n, "es par")
    sumapares=sumapares
  else:
    #print(n," es impar")
    sumaimpares=sumaimpares+n

print("El total de impares es: ",sumaimpares)
print("El total de pares es: ",sumapares)
print("El total general es: ",sumaimpares+sumapares)