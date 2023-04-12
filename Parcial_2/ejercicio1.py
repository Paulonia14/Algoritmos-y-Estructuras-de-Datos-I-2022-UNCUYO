#Nombre y apellido: Paula Daniela Martinez
#Legajo: 13866
#Mail: martinezpaula1488@gmail.com

from linkedlist import *
import binarytree

def findCommonAncestor(Tree,NodoA,NodoB):
  #Entrada: Un arbol binario de búsqueda y dos Nodos
  #Salida: El valor del primer ancestro en común
  if Tree.root==None:
    return None
  element=None
  listAncestorsA=LinkedList()
  listAncestorsB=LinkedList()
  element=findNodes(Tree,NodoA,NodoB,element,Tree.root,listAncestorsA,listAncestorsB)
  return element

def findNodes(B,NodoA,NodoB,element,current,listAncestorsA,listAncestorsB):
  #Recorre el árbol buscando los nodos A y B
  if current!=None:
    if current.key==NodoA.key:
      listAncestorsA=listAncestors(B,current,listAncestorsA)
    elif current.key==NodoB.key:
      listAncestorsB=listAncestors(B,current,listAncestorsB)
    findNodes(B,NodoA,NodoB,element,current.leftnode,listAncestorsA,listAncestorsB)
    findNodes(B,NodoA,NodoB,element,current.rightnode,listAncestorsA,listAncestorsB)
    #Busca el primer ancestro en común
    for i in range(0,length(listAncestorsA)):
      for j in range(0,length(listAncestorsB)):
        if access(listAncestorsA,i)==access(listAncestorsB,j):
          element=binarytree.access(B,access(listAncestorsA,i))
          return element
  return element
  
def listAncestors(B,current,L):
  #Guarda los ancestros de un nodo en una lista
  if current.parent!=None:
    insert(L,current.parent.key,length(L))
    listAncestors(B,current.parent,L)
  return L
