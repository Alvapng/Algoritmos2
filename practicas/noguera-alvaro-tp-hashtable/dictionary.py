class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Dictionary:
    def __init__(self, m):
        self.table = [None] * m  
        self.m = m               
        self.count = 0   


#--------------------------------------------------------------------------------------------
# EJERCICIO 1
#--------------------------------------------------------------------------------------------

def insert(D, key, value):
    nuevoNodo = Node(key,value)

    posicion = key % D.m

    if(D.table[posicion] == None):
        D.table[posicion] = nuevoNodo
    else:
        nuevoNodo.next = D.table[posicion]
        D.table[posicion] = nuevoNodo    

    return D

def search(D,key):
    posicion = key % D.m
    actual = D.table[posicion]
    while(actual != None):
        if(actual.key == key):
            return key
        actual = actual.next
    return None

def delete(D, key):
    posicion = key % D.m
    actual = D.table[posicion]
    anterior = None
    
    while(actual != None):
        if(actual.key == key):
            if(anterior == None):
                D.table[posicion] = actual.next
            else:
                anterior.next = actual.next
            
            return D  
            
        anterior = actual
        actual = actual.next
        
    return D  


#--------------------------------------------------------------------------------------------
# EJERCICIO 4
#--------------------------------------------------------------------------------------------

def permutaciones(S,P):
    if(len(S) != len(P)):
        return False

    m = 127
    D = Dictionary(m)
    for c in S:
        key = ord(c)

        frecuenciaActual = search(D,key)

        if(frecuenciaActual == None):
            insert(D,key,1)
        else:
            frecuenciaActual += 1
            insert(D,key,frecuenciaActual)    

    for c in P:
        key = ord(c)
        frecuencia = search(D,key)        

        if(frecuencia == None or frecuencia == 0):
            return False

        insert(D,key,frecuencia-1)

    return True    


#--------------------------------------------------------------------------------------------
# EJERCICIO 5
#--------------------------------------------------------------------------------------------

def repetidos(L):
    m = len(L)
    D = Dictionary(m)

    for n in L:
        if(search(D,n) != None):
            return False
        insert(D,n,True)

    return True    


#--------------------------------------------------------------------------------------------
# EJERCICIO 6
#--------------------------------------------------------------------------------------------

def correo(L,m):
    hashVal = 0
    for i in range(0,len(L)):
        hashVal += ord(L[i]) * (31**i)

    return hashVal % m


#--------------------------------------------------------------------------------------------
# EJERCICIO 7
#--------------------------------------------------------------------------------------------

def compresion(L):
    contador = 1
    D = []
    for i in range(0,len(L)-1):
        if(L[i] == L[i + 1]):
            contador += 1
        else:
            D.append(L[i])
            D.append(str(contador))  
            contador = 1

    D.append(L[-1])    
    D.append(str(contador))    
    resultado = "".join(D)

    if(len(resultado)>=len(L)):
        return L
    else:
        return resultado          


#--------------------------------------------------------------------------------------------
# EJERCICIO 8
#--------------------------------------------------------------------------------------------



def ocurrencia(L,cadena):
    k = len(cadena)

    hashCadena = correo(cadena,1000)

    for i in range(0,len(L)- k + 1):
        ventana = L[i:i+k]
        hashVentana = correo(ventana,1000)

        if(hashCadena == hashVentana):
            if(ventana == cadena):
                return i

    return -1        


#--------------------------------------------------------------------------------------------
# EJERCICIO 9
#--------------------------------------------------------------------------------------------        

def es_subconjunto(S, T):
    m = len(T) 
    D = Dictionary(m)
    
    for elemento in T:
        insert(D, elemento, elemento)
        
    for elemento in S:
        if(search(D, elemento) == None):
            return False
            
    return True