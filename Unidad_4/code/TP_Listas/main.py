from algo1 import *
from mylinkedlist import *

# - Ejercicio 1 -
def intercalarListas(A,B,C): # b)
  #Llenar una lista C con valores intercalados de las listas A y B
  currentA=A.head
  currentB=B.head
  size=length(A)+length(B)
  checkA=True
  for i in range (0,size):
    if (checkA==True):
      insert(C,currentA.value,i)
      currentA=currentA.nextNode
      checkA=False
    else:
      insert(C,currentB.value,i)
      currentB=currentB.nextNode
      checkA=True

def eliminarPares(L,L2): # c) 
  #Eliminar de la segunda lista los elementos pares de la primer lista
  current=L.head
  while current!=None:
    if (current.value%2==0):
      delete(L2,current.value)
    current=current.nextNode
      
def buscarImpares(L,L2): # d)
  #Crear una lista con los elementos impares de L
  current=L.head
  cont=0
  while current!=None:
    if (current.value%2!=0):
      insert(L2,current.value,cont)
      cont+=1
    current=current.nextNode
  
def sacarRepetidos(L): # e)
  #Sacar elementos repetidos de una lista
  current=L.head
  while current!=None:
    current2=L.head
    while current2!=None:
      if current!=current2 and current.value==current2.value:
        delete(L,current.value)
      current2=current2.nextNode
    current=current.nextNode

# - Ejercicio 2 -
def printListEmpleados(L):
  #Imprimir lista de empleados
  current=L.head
  while current!=None:
    print(current.value.nombre, end=", ")
    print(current.value.edad, end=", ")
    print(current.value.nroLegajo)
    current=current.nextNode

# - Ejercicio 3 -
def sacarLegajosDuplicados(L): # a)
  #Sacar los numeros de legajos duplicados de una lista de empleados
  current=L.head
  while current!=None:
    current2=L.head
    while current2!=None:
      if current!=current2 and current.value.nroLegajo==current2.value.nroLegajo:
        delete(L,current2.value)
      current2=current2.nextNode
    current=current.nextNode

# - Ejercicio 4 - 
def invertirLista(L):
  #ordenar de manera inversa los elementos (nodos) de una lista
  newL=LinkedList()
  size=length(L)
  current=L.head
  for i in range(0,size):
    aux=current.value
    add(newL,aux)
    current=current.nextNode
    delete(L,aux)
  current=newL.head
  for i in range(0,size):
    insert(L,current.value,i)
    current=current.nextNode

# - Ejercicio 1 -
A=LinkedList()
B=LinkedList()

add(A,678)
add(A,3)
add(A,22)
add(A,54)
add(A,345)
add(A,89)
add(A,67)
add(A,3)
add(A,45)
add(A,24)
print("Lista A: ")
printList(A)

add(B,33)
add(B,12)
add(B,567)
add(B,234)
add(B,15)
add(B,12)
add(B,59)
add(B,64)
add(B,34)
add(B,46)
print("Lista B: ")
printList(B)

# b)
C=LinkedList()
intercalarListas(A,B,C)
print("Lista C:")
printList(C)

# c)
eliminarPares(A,C)
print("Lista C sin elementos pares de la lista A: ")
printList(C)

# d)
D=LinkedList()
buscarImpares(C,D)
print("Lista D: ")
printList(D)

# e)
sacarRepetidos(A)
#añadirle al final todos los elementos de B que se encuentren entre 50 y 100
size=length(A)
current=B.head
while current!=None:
  if current.value>50 and current.value<100:
    insert(A,current.value,size)
    size+=1
  current=current.nextNode
print("Lista A cambiada: ")
printList(A)
print("")

# - Ejercicio 2 - 
class LinkedListEmpleado:
  head=None
class Empleado:
  nombre=None
  edad=None
  nroLegajo=None
class NodeEmpleado:
  value=Empleado
  nextNode=None

listaEmpleados=LinkedListEmpleado()

dato=Empleado()
dato.nombre="Luis Esteban"
dato.edad=32
dato.nroLegajo=7
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Eduardo Ángel"
dato.edad=34
dato.nroLegajo=2
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Pedro César"
dato.edad=45
dato.nroLegajo=8
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Luis Esteban"
dato.edad=32
dato.nroLegajo=7
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Pedro Augusto"
dato.edad=40
dato.nroLegajo=9
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Juan Carlos"
dato.edad=23
dato.nroLegajo=5
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Luis Esteban"
dato.edad=32
dato.nroLegajo=7
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Juan Carlos"
dato.edad=23
dato.nroLegajo=5
add(listaEmpleados,dato)

dato=Empleado()
dato.nombre="Eduardo Ángel"
dato.edad=34
dato.nroLegajo=2
add(listaEmpleados,dato)

printListEmpleados(listaEmpleados)
print("")

# - Ejercicio 3 -
# a)
sacarLegajosDuplicados(listaEmpleados)
print("No duplicados")
printListEmpleados(listaEmpleados)

# b)
nuevoEmpleado=Empleado()
nuevoEmpleado.nombre="Ernesto Andrés"
nuevoEmpleado.edad=55
nuevoEmpleado.nroLegajo=6
current=listaEmpleados.head
pos=0
while current!=None:
  if current.value.nroLegajo==7:
    insert(listaEmpleados,nuevoEmpleado,pos)
  pos+=1
  current=current.nextNode
print("")
print("Lista con nuevo empleado: ")
printListEmpleados(listaEmpleados)

# c)
current=listaEmpleados.head
while current!=None:
  if current.value.nroLegajo==9:
    aux=current.value
    delete(listaEmpleados,current.value)
  current=current.nextNode
current=listaEmpleados.head
pos=0
while current!=None:
  if current.value.nroLegajo==8:
    insert(listaEmpleados,aux,pos+1)
  pos+=1
  current=current.nextNode
print("")
print("Lista resultante:")
printListEmpleados(listaEmpleados)

# - Ejercicio 4 -
print("")
print("Lista A:")
printList(A)
invertirLista(A)
print("Lista A invertida: ")
printList(A)

print("")
print("Lista C:")
printList(C)
invertirLista(C)
print("Lista C invertida: ")
printList(C)