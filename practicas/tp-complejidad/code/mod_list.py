class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None


def add(L,element):
    n = Node()
    n.value = element
    n.nextNode = L.head
    L.head = n

def search(L,element):
    n = Node()
    n = L.head
    posicion = 0
    while n != None:
        if(n.value == element):
            return posicion
        else:
            n = n.nextNode
            posicion = posicion + 1   
    return None
# 

def length(L):
    n = Node()
    n = L.head
    tamaño = 0
    while n != None:
        tamaño = tamaño + 1
        n = n.nextNode
    return tamaño    

def insert(L,element,position):
    if(position >= 0 and position <= length(L)):
        n = Node()
        n.value = element
        if (position == 0):
           n.nextNode = L.head
           L.head = n
        else:
            actual = L.head    
            for i in range(0,position-1):
                actual = actual.nextNode
            n.nextNode = actual.nextNode
            actual.nextNode = n    
        return position
    else:
        return None


def delete2(L,position):
    if(L.head == None or position > length(L)):
        return None

    if(position == 0):
        L.head = L.head.nextNode
        return position

    else:

        actual = L.head

        for i in range(0, position - 1):
            actual = actual.nextNode

        eliminar = actual.nextNode

        actual.nextNode = eliminar.nextNode   


def delete(L, element):
    if(L.head == None):
        return None
    elif(L.head.value == element):
        L.head = L.head.nextNode
    else:

        anterior = L.head
        actual = L.head.nextNode

        for i in range(0, length(L)):
            if (actual.value == element):
                anterior.nextNode = actual.nextNode
                return i
            anterior = actual
            actual = actual.nextNode    
        return None    
    
def acces(L,position):
    actual = L.head   
    if(position >= 0 and position < length(L)):
        for i in range(0, position):
            actual = actual.nextNode
        return actual.value    
    else:
        return None    
    
def update(L, element, position):    
    actual = L.head
    if(position >= 0 and position < length(L)):
        for i in range(0, position):
            actual = actual.nextNode
        actual.value = element   
        return position
    else:
        return None 
    

def move(L,position_orig,position_dest):
    aux1 = acces(L,position_orig)
    aux2 = acces(L, position_dest)
    update(L, aux2, position_orig)
    update(L, aux1, position_dest)

def show(L):
    for n in range(0, length(L)):
        print(acces(L,n), end=" ")
    print("")        


