from mod_list import *
from mod_ordAvanzados import *

#Funcion que verifica la presencia de la suma
def contiene_sum(L,n):
    #Aplcacion del mergeSort
    L = mergeSort(L)
    #Iniciacion de los punteros
    posicion_izq = 0
    posicion_der = length(L) - 1
    encontrado = False
    #Bucle que va haciendo la verificion con sus respectivas condiciones
    while(posicion_izq < posicion_der):
        el_izq = acces(L,posicion_izq)
        el_der = acces(L,posicion_der)
        if((el_izq + el_der) == n):
            return True
        if((el_izq + el_der) > n):
            posicion_der = posicion_der - 1
        if((el_izq + el_der) < n):
            posicion_izq = posicion_izq + 1 
    return False        

#Pruebas:
L = LinkedList()

add(L,1)
add(L,2)
add(L,3)
add(L,4)
add(L,5)
add(L,6)
add(L,10)


print("Contiene la suma? ",contiene_sum(L,10))
