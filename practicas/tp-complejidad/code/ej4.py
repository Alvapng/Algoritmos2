from mod_list import *

#Funcion que hace el ordenamiento

def ord(L):

    #Identificacion del elemnto central y creacion de la lista donde se guardarn los elementos menores al elemento central
    menores = LinkedList()
    el_central = acces(L,(length(L) // 2 ))
    print("Elemento central: ", el_central)

    #Bucle que guarda los elementos menores al elemento central

    for i in range(0,length(L)):
        elemento_Actual = acces(L,i)
        if(elemento_Actual < el_central):
            el_menor = LinkedList()
            add(el_menor,i)
            add(el_menor, elemento_Actual)
            add(menores, el_menor)

    destino = 0

    #Bucle que hace los intercambios necesarios
    for i in range(0,length(menores)//2):
        menor = acces(menores,i)
        elemento_menor = acces(menor,0)
        posicion = acces(menor, 1)
        move(L,destino,posicion)     
        destino = destino + 1
    return L


#Pruebas
L = LinkedList()
add(L,1)
add(L,7)
add(L,5)
add(L,6)
add(L,4)
add(L,8)
add(L,2)
      

print("Lista original:")
show(L)
ord(L)
print("Lista ordenada: ")
show(L)
