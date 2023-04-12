###########################################
#funciones o subprocesos
###########################################
import algo1

def access(Array,position):   # 3 OE
  return Array[position]      # 2 OE


def search(Array,element):  # 3 OE
  n=len(Array)              # 2 OE
  for i in range(0,n):      # 3 OE + n OE
    if Array[i]==element:   # n OE
      return i              # 2n OE
  return None               # 2 OE

def insert(Array,element,position):  # 4 OE
  n=len(Array)                       # 2 OE
  if position>=n:                    # 1 OE
    return None                      # 2 OE
  ArrayR=algo1.Array(n,0)            # 2 OE
  for i in range(0,n):               # 3 OE + n OE
    ArrayR[i]=Array[i]               # n OE
  for i in range (position,n-1):     # 3 OE + n OE
    ArrayR[i+1]=Array[i]             # n OE
  ArrayR[position]=element           # 1 OE
  for i in range(0,n):               # 3 OE + n OE
    Array[i]=ArrayR[i]               # n OE
  return position                    # 2 OE

def delete(Array,element):         # 3 OE
  position=search(Array,element)   # 4 OE
  if position==None:               # 1 OE
    return None                    # 2 OE
  n=len(Array)                     # 2 OE
  ArrayR=algo1.Array(n,0)          # 2 OE
  for i in range(0,position):      # 3 OE + n OE
    ArrayR[i]=Array[i]             # n OE
  for i in range(position,n-1):    # 3 OE + n OE
    ArrayR[i]=Array[i+1]           # n OE
  for i in range(0,n):             # 3 OE + n OE
    Array[i]=ArrayR[i]             # n OE
  return position                  # 2 OE

def length(Array):
  cont=0
  n=len(Array)
  for i in range(0,n):
    if Array[i]!=None:
      cont+=1
  return cont

