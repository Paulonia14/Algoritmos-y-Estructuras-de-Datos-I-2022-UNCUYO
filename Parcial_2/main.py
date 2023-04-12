import binarytree
from linkedlist import *
from ejercicio1 import *
from ejercicio2 import *

# -- Para probar valores --
# -- Ejercicio 1 --

B=binarytree.BinaryTree()

binarytree.insert(B,8,8);binarytree.insert(B,"hola",5);binarytree.insert(B,"aa",3);binarytree.insert(B,2,2);binarytree.insert(B,4,4);binarytree.insert(B,6,6)
binarytree.insert(B,7,7);binarytree.insert(B,"a",9);binarytree.insert(B,11,11);binarytree.insert(B,10,10)
L1=LinkedList()
L1=binarytree.traverseInPostOrder(B)
printList(L1)

NodoA=binarytree.BinaryTreeNode()
NodoB=binarytree.BinaryTreeNode()
NodoA.key=2;NodoA.value=2
NodoB.key=7;NodoA.value=7
a=findCommonAncestor(B,NodoA,NodoB)
print("Common ancestor a :",a)  

NodoA=binarytree.BinaryTreeNode()
NodoB=binarytree.BinaryTreeNode()
NodoA.key=2;NodoA.value=2
NodoB.key=4;NodoA.value=4
b=findCommonAncestor(B,NodoA,NodoB)
print("Common ancestor b :",b)

NodoA=binarytree.BinaryTreeNode()
NodoB=binarytree.BinaryTreeNode()
NodoA.key=4;NodoA.value=4
NodoB.key=11;NodoA.value=11
c=findCommonAncestor(B,NodoA,NodoB)
print("Common ancestor c :",c)

NodoA=binarytree.BinaryTreeNode()
NodoB=binarytree.BinaryTreeNode()
NodoA.key=10;NodoA.value=10
NodoB.key=11;NodoA.value=11
d=findCommonAncestor(B,NodoA,NodoB)
print("Common ancestor d :",d)

NodoA=binarytree.BinaryTreeNode()
NodoB=binarytree.BinaryTreeNode()
NodoA.key=2;NodoA.value=2
NodoB.key=12;NodoA.value=12
e=findCommonAncestor(B,NodoA,NodoB)
print("Common ancestor e :",e)


# -- Ejercicio 2 --
L=LinkedList()

insert(L,"8",length(L))
insert(L,"+",length(L))
insert(L,"1",length(L))
insert(L,"-",length(L))
insert(L,"5",length(L))
insert(L,"*",length(L))
insert(L,"4",length(L))
insert(L,"/",length(L))
insert(L,"3",length(L))
printList(L)

A=calculate_expression(L)
print(A)


