#Nombre y apellido: Paula Daniela Martinez
#Legajo: 13866
#Mail: martinezpaula1488@gmail.com

from linkedlist import *

def calculate_expression(L):
  #Se crea una lista con los operadores
  operators=LinkedList()
  add(operators,"+")
  add(operators,"-")
  add(operators,"*")
  add(operators,"/")
  operate(L,operators.head)
  #Trunco el resultado con int
  return int(L.head.value)

def operate(L,operation):
  current=L.head.nextNode
  prevNode=L.head
  prevprevNode=L.head
  cont=0
  while current.nextNode!=None:
    if current.value==operation.value:
      if operation.value=="/":
        element=float(prevNode.value)/float(current.nextNode.value)
      elif operation.value=="*":
        element=float(prevNode.value)*float(current.nextNode.value)
      elif operation.value=="-":
        element=float(prevNode.value)-float(current.nextNode.value)
      elif operation.value=="+":
        element=float(prevNode.value)+float(current.nextNode.value)
      prevprevNode.nextNode=current.nextNode.nextNode
      insert(L,element,cont)
    if prevNode!=L.head:
      prevprevNode=prevprevNode.nextNode
    prevNode=prevNode.nextNode
    current=current.nextNode
    cont+=1
  #Si todavía quedan operadores, llama a la funcion con el siguiente operador siguiendo el orden de precedencia aritmética. Si no quedan más operadores retorno la lista que tendrá el resultado en su cabeza
  if operation.value!="+":
    operate(L,operation.nextNode)
  else:
    return L
    
