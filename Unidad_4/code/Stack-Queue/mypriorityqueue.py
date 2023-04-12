from mylinkedlist import *

class PriorityQueue:
  head=None

class PriorityNode:
  value=None
  nextNode=None
  priority=None

def enqueue_priority(Q,element,priority):
  #Agrega un elemento a la cola Q con su prioridad
  add(Q,element)
  Q.head.priority=priority
  return 0

def dequeue_priority(Q):
  #extrae el primer elemento de la cola Q con la mayor prioridad
  size=length(Q)
  if (size==0):
    return None
  maximo=Q.head.priority
  current=Q.head
  for i in range(0,size):
    if (current.priority>=maximo):
      maximo=current.priority
      element=current.value
      position=i
    current=current.nextNode
  current=Q.head
  if (size==1):
    Q.head=None
  elif (position==0):
    Q.head=current.nextNode
  else:
    for i in range(0,position-1):
      current=current.nextNode
    current.nextNode=current.nextNode.nextNode
  return element
