from mylinkedlist import *

def BubbleSort(L):
  if L.head==None:
    return None
  size=length(L)
  for i in range(0,length(L)):
    for j in range(0,size-1):
      #Busca los elementos en la posición actual y la siguiente(nextNode) con access
      #Si se usa current.value se rompe
      if access(L,j)>access(L,j+1):
        move(L,j,j+1)
      printList(L)
    size=size-1 #Esto es para que no verifique los que ya están ordenados al final
    
def SelectionSort(L):
  if L.head==None:
    return None
  size=length(L)
  inicio=0
  for i in range(0,size):
    menor=access(L,i)
    for j in range(inicio,size):
      if access(L,j)<=menor:
        menor=access(L,j)
        positionM=j
        printList(L)
    move(L,positionM,i)
    inicio+=1 
    #para que no verifique los que ya están ordenados al inicio
    
def InsertionSort(L):
  if L.head==None:
    return None
  for i in range(1,length(L)):
    for j in range(0,i):
      if access(L,i)<access(L,j):
        elementDel=deletePosition(L,i) #Esta función retorna el elemento que se eliminó
        insert(L,elementDel,j)
        #printList(L)
      printList(L)
        
        
def quehago(L):
  j=1
  while(j<length(L)):
    i=j
    a=access(L,i)
    b=access(L,i-1)
    while i>0 and a<b:
      update(L,a,i-1)
      update(L,b,i)
      i=i-1
      a=access(L,i)
      b=access(L,i-1)
      printList(L)
    j=j+1
    #printList(L)