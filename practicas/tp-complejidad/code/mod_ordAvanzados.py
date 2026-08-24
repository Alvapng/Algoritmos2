from mod_list import *

def quickSort(L):
    if(length(L) <= 1):
        return L
    
    pivote = acces(L,length(L)-1)

    subIzq = izq(L,pivote)
    subDer = der(L,pivote)

    return concatenar(quickSort(subIzq),pivote,quickSort(subDer))

def izq(L, pivote):
    subListaIzq = LinkedList()
    for n in range(0, length(L)-1):
        if(acces(L,n) <= pivote):
            add(subListaIzq,acces(L,n))
    return subListaIzq        

def der(L,pivote):
    subListaDer = LinkedList()
    for n in range(0, length(L)-1):
        if(acces(L, n) > pivote):
            add(subListaDer,acces(L,n))        
    return subListaDer


def concatenar(Lizq,pivote,Lder):
    nuevaLista = LinkedList()

    for n in range(0,length(Lizq)):
        insert(nuevaLista,acces(Lizq,n),length(nuevaLista))

    insert(nuevaLista,pivote,length(nuevaLista))

    for n in range(0,length(Lder)):
        insert(nuevaLista,acces(Lder,n),length(nuevaLista)) 

    return nuevaLista         


def mergeSort(L):

    if(length(L) <= 1):
        return L
    
    medio = length(L) // 2

    izquierda = LinkedList()
    derecha = LinkedList()

    for i in range(0,medio):
        insert(izquierda,acces(L,i),length(izquierda))

    for i in range(medio, length(L)):
        insert((derecha),acces(L,i),length(derecha))

    izq_ordenada = mergeSort(izquierda)
    der_ordenada = mergeSort(derecha)

    return merge(izq_ordenada,der_ordenada)


def merge(izq,der):

    lista_mezclada = LinkedList()

    i = 0
    j = 0

    while(i < length(izq) and j < length(der)):
        val_izq = acces(izq,i)
        val_der = acces(der,j)

        if val_izq <= val_der:
            insert(lista_mezclada, val_izq, length(lista_mezclada))
            i = i + 1
        else:
            insert(lista_mezclada, val_der, length(lista_mezclada))
            j = j + 1

    while i < length(izq):
        insert(lista_mezclada, acces(izq, i), length(lista_mezclada))
        i = i + 1

    while j < length(der):
        insert(lista_mezclada, acces(der, j), length(lista_mezclada))
        j = j + 1

    return lista_mezclada    


def heapSort(L):

    n = length(L)

    for i in range(n // 2 - 1, -1, -1):
        heapify(L, n, i)

    for i in range(n - 1, 0, -1):
        move(L, 0, i)
        
        heapify(L, i, 0)
        
    return L    



def heapify(L,tamaño_heap, i):
    mayor = i
    hijo_izq = 2 * i + 1
    hijo_der = 2 * i + 2

    if hijo_izq < tamaño_heap and acces(L, hijo_izq) > acces(L, mayor):
        mayor = hijo_izq

    if hijo_der < tamaño_heap and acces(L, hijo_der) > acces(L, mayor):
        mayor = hijo_der

    if mayor != i:
        move(L, i, mayor)

        heapify(L, tamaño_heap, mayor)
