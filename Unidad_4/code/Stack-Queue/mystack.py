from mylinkedlist import *

def push(S,element):
  #Agrega un elemento al comienzo de la pila S
  add(S,element)

def pop(S):
  #Extrae el primer elemento de la pila S
  size=length(S)
  if (size==0):
    return
  element=S.head.value
  S.head=S.head.nextNode
  return element
